from tkinter.filedialog import askopenfilename
filename = askopenfilename(title='select beat saber map .zip', filetypes=[
                    ("beat saber map", ".zip"),
                ])

if filename=='':
   import ctypes
   import sys
   sys.exit()
   
pathname= filename[:filename.rfind("/")]
import random
num = random.random()
tempname= pathname + "/BeatSaberToOsuConverter" + str(num)
import zipfile
with zipfile.ZipFile(filename,"r") as zip_ref:
    zip_ref.extractall(tempname)
import os
os.chdir(tempname)

import shutil
if os.path.exists('Info.dat') == False:
   import ctypes
   ctypes.windll.user32.MessageBoxW(0, "There is no Info.dat in it", "Not a beat saber .zip file", 1)
   shutil.rmtree(tempname)
   import sys
   sys.exit()


with open('Info.dat', 'r') as file:
   info = file.read().replace('\n', '')

def convert(beatspermin, bstiming):
   unit = float(60 / float(beatspermin) / 8)
   stuff = float(bstiming)*8
   return(float(stuff*1000*unit))
#   protected double ConvertTime(int timeMs) 
# { 
#     var unit = 60.0 / bpm / 8.0; 
#     var sectionIdx = (int)Math.Round(((timeMs) / 1000.0 / unit)); 
#     return Math.Round(sectionIdx / 8.0, 3, MidpointRounding.AwayFromZero); 
# } 

songName = (info[info.find("_songName")+13:info.find("_songSubName")-4])
songAuthorName = (info[info.find("_songAuthorName")+19:info.find("_levelAuthorName")-4])
levelAuthorName = (info[info.find("_levelAuthorName")+20:info.find("_beatsPerMinute")-4])
bpm = (info[info.find("_beatsPerMinute")+18:info.find("_songTimeOffset")-3])
FileNamer = songAuthorName + " - " + songName + " (" + levelAuthorName + ") [BeatSaberToOSU]"
print("Song name: " + songName + "\nSong author: " + songAuthorName + "\nBeatmap author: " + levelAuthorName + "\nBPM: " + bpm)

os.chdir(pathname)
if os.path.exists(FileNamer + '.osz') == True:
   import ctypes  # An included library with Python install.   
   ctypes.windll.user32.MessageBoxW(0, FileNamer + '.osu already exists, delete it and rerun to regenerate', "hello", 1)
   shutil.rmtree(tempname)
   import sys
   sys.exit()
   
os.chdir(tempname)

# create string from file
def difficulty(filename, HPDrainRate, CircleSize, OverallDifficulty, ApproachRate, SliderMultiplier, SliderTickRate):

   filenamedat=filename + '.dat'
   filenameosu=songAuthorName + ' - ' + songName + ' [' + filename + '] (' + levelAuthorName + ' [BeatSaberToOSU]).osu'
   
   if not os.path.exists(filenamedat):
      return(filenamedat + " Doesn't exist, skipping")
   if os.path.exists(filenameosu):
      return(filenameosu + ' already exists, skipping. Delete it if you want to regenerate it.')
      
   with open(filenamedat, 'r') as file:
      bs = file.read().replace('\n', '')

      
   # creates what i think is lists? from stuffs
   time = [i for i in range(len(bs)) if bs.startswith("_time", i)]
   lineIndex = [i for i in range(len(bs)) if bs.startswith("_lineIndex", i)]
   lineLayer = [i for i in range(len(bs)) if bs.startswith("_lineLayer", i)]
   #type = [i for i in range(len(bs)) if bs.startswith("_type", i)]
   value = [i for i in range(len(bs)) if bs.startswith("_value", i)]
   cutDirection = [i for i in range(len(bs)) if bs.startswith("_cutDirection", i)]



   # bpms = float(bpm)/60000
   # print(bpms)
   # the beginning of the osu file with dumb parameters but idk how to change them so circles are really slow and dumb and i dont like them
   osu = "osu file format v14\n\n[General]\nAudioFilename: song.ogg\nAudioLeadIn: 0\nPreviewTime: -1\nCountdown: 0\nSampleSet: Normal\nStackLeniency: 0.5\nMode: 0\nLetterboxInBreaks: 0\nWidescreenStoryboard: 0\n\n[Editor]\nDistanceSpacing: 1.1\nBeatDivisor: 4\nGridSize: 8\nTimelineZoom: 1.6\n\n[Metadata]\nTitle:" + songName + "\nTitleUnicode:" + songName +"\nArtist:" + songAuthorName + "\nArtistUnicode:" + songAuthorName + "\nCreator:" + levelAuthorName + "\nVersion:" + filename + "\nSource:\nTags:BeatSaber\nBeatmapID:0\nBeatmapSetID:-1\n\n[Difficulty]\nHPDrainRate:" + str(HPDrainRate) + "\nCircleSize:" + str(CircleSize) + "\nOverallDifficulty:" + str(OverallDifficulty) + "\nApproachRate:" + str(ApproachRate) + "\nSliderMultiplier:" + str(SliderMultiplier) + "\nSliderTickRate:" + str(SliderTickRate) + "\n\n[Events]\n//Background and Video events\n//Break Periods\n//Storyboard Layer 0 (Background)\n//Storyboard Layer 1 (Fail)\n//Storyboard Layer 2 (Pass)\n//Storyboard Layer 3 (Foreground)\n//Storyboard Layer 4 (Overlay)\n//Storyboard Sound Samples\n\n[TimingPoints]\n0," + str(30000/float(bpm)) + ",4,1,0,100,1,0\n\n\n[HitObjects]\n"

   if len(value) > 0:
      #for i in range(len(value)):
         #osu = osu + '320,240,' + str(convert(bpm, bs[(time[i]+8):(time[i]+20)])) + ',1,0,0:0:0:0:\n'
      del time[:len(value)]

   if len(time) > len(lineLayer):
      #for i in range(len(lineLayer), len(time)):
         #osu = osu + '320,240,' + str(convert(bpm, bs[(time[i]+8):(time[i]+20)])) + ',1,0,0:0:0:0:\n'
      del time[len(lineLayer):len(time)]
      
   osu = osu + str((int(bs[lineIndex[0]+13])*100)+85) + ',' + str((int(bs[lineLayer[0]+13])*100)+70) + ',' + str(convert(bpm, bs[(time[0]+8):(time[0]+20)])) + ',1,0,0:0:0:0:\n'
   
   for i in range(1, len(time)):
      if abs(float(bs[(time[i]+8):(time[i]+20)])-float(bs[(time[i-1]+8):(time[i-1]+20)])) > 0.01:
         osu = osu + str((int(bs[lineIndex[i]+13])*100)+85
         #+((4-int(bs[cutDirection[i]+16]))*10)
         ) + ',' + str((int(bs[lineLayer[i]+13])*100)+70
         #-((4-int(bs[cutDirection[i]+16]))*10)
         ) + ',' + str(convert(bpm, bs[(time[i]+8):(time[i]+20)])) + ',1,0,0:0:0:0:\n'


   with open(filenameosu, "w+") as myfile:
      myfile.write(osu)
      
   return(filenameosu + ' generated from ' + filenamedat)

#HPDrainRate, CircleSize, OverallDifficulty, ApproachRate, SliderMultiplier, SliderTickRate
print(difficulty('Normal',             2,    2,    7.5,    8.5, 1.4, 1))
print(difficulty('Hard',               3,    3,    7.5,  9.5, 2.5, 1))
print(difficulty('Expert',             3.5,  3.5,  7.5,    9.75, 3.2, 1))
print(difficulty('ExpertPlus',         4,    4,    7.5,  10, 3.3, 1))

print(difficulty('OneSaberNormal',     2,    2,    7.5,    8.5, 1.4, 1))
print(difficulty('OneSaberHard',       3,    3,    7.5,  9.5, 2.5, 1))
print(difficulty('OneSaberExpert',     3.5,  3.5,  7.5,    9.75, 3.2, 1))
print(difficulty('OneSaberExpertPlus', 4,    4,    7.5,  10, 3.3, 1))

print(difficulty('NoArrowsNormal',     2,    2,    7.5,    8.5, 1.4, 1))
print(difficulty('NoArrowsHard',       3,    3,    7.5,  9.5, 2.5, 1))
print(difficulty('NoArrowsExpert',     3.5,  3.5,  7.5,    9.75, 3.2, 1))
print(difficulty('NoArrowsExpertPlus', 4,    4,    7.5,  10, 3.3, 1))

print(difficulty('90DegreeNormal',     2,    2,    7.5,    8.5, 1.4, 1))
print(difficulty('90DegreeHard',       3,    3,    7.5,  9.5, 2.5, 1))
print(difficulty('90DegreeExpert',     3.5,  3.5,  7.5,    9.75, 3.2, 1))
print(difficulty('90DegreeExpertPlus', 4,    4,    7.5,  10, 3.3, 1))

print(difficulty('360DegreeNormal',    2,    2,    7.5,    8.5, 1.4, 1))
print(difficulty('360DegreeHard',      3,    3,    7.5,  9.5, 2.5, 1))
print(difficulty('360DegreeExpert',    3.5,  3.5,  7.5,    9.75, 3.2, 1))
print(difficulty('360DegreeExpertPlus', 4,    4,    7.5,  10, 3.3, 1))

os.chdir(pathname)
shutil.make_archive(FileNamer, 'zip', tempname)
from pathlib import Path
p = Path(pathname + '/' + FileNamer + '.zip')
p.rename(p.with_suffix('.osz'))
shutil.rmtree(tempname)
print('Done!')