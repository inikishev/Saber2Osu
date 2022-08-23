# it needs to just not work when file exists
import os



def convert(beatspermin, bstiming):
   unit = float(60 / float(beatspermin) / 8)
   stuff = float(bstiming)*8
   return(float(stuff*1000*unit))

with open('Info.dat', 'r') as file:
   info = file.read().replace('\n', '')



songName = (info[info.find("_songName")+13:info.find("_songSubName")-4])
songAuthorName = (info[info.find("_songAuthorName")+19:info.find("_levelAuthorName")-4])
levelAuthorName = (info[info.find("_levelAuthorName")+20:info.find("_beatsPerMinute")-4])
bpm = (info[info.find("_beatsPerMinute")+18:info.find("_songTimeOffset")-3])

print("Song name: " + songName + "\nSong author: " + songAuthorName + "\nBeatmap author: " + levelAuthorName + "\nBPM: " + bpm)

   
#   protected double ConvertTime(int timeMs) 
# { 
#     var unit = 60.0 / bpm / 8.0; 
#     var sectionIdx = (int)Math.Round(((timeMs) / 1000.0 / unit)); 
#     return Math.Round(sectionIdx / 8.0, 3, MidpointRounding.AwayFromZero); 
# } 

# create string from file
def difficulty(filename, HPDrainRate, CircleSize, OverallDifficulty, ApproachRate, SliderMultiplier, SliderTickRate):

   filenamedat=filename + '.dat'
   filenameosu=filename + '.osu'
   
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
   #cutDirection = [i for i in range(len(bs)) if bs.startswith("_cutDirection", i)]



   # bpms = float(bpm)/60000
   # print(bpms)
   # the beginning of the osu file with dumb parameters but idk how to change them so circles are really slow and dumb and i dont like them
   osu = "osu file format v14\n\n[General]\nAudioFilename: audio.mp3\nAudioLeadIn: 0\nPreviewTime: -1\nCountdown: 0\nSampleSet: Normal\nStackLeniency: 0.7\nMode: 0\nLetterboxInBreaks: 0\nWidescreenStoryboard: 0\n\n[Editor]\nDistanceSpacing: 1.1\nBeatDivisor: 4\nGridSize: 8\nTimelineZoom: 1.6\n\n[Metadata]\nTitle:" + songName + "\nTitleUnicode:" + songName +"\nArtist:" + songAuthorName + "\nArtistUnicode:" + songAuthorName + "\nCreator:" + levelAuthorName + "\nVersion:" + filename + "\nSource:\nTags:BeatSaber\nBeatmapID:0\nBeatmapSetID:-1\n\n[Difficulty]\nHPDrainRate:" + str(HPDrainRate) + "\nCircleSize:" + str(CircleSize) + "\nOverallDifficulty:" + str(OverallDifficulty) + "\nApproachRate:" + str(ApproachRate) + "\nSliderMultiplier:" + str(SliderMultiplier) + "\nSliderTickRate:" + str(SliderTickRate) + "\n\n[Events]\n//Background and Video events\n//Break Periods\n//Storyboard Layer 0 (Background)\n//Storyboard Layer 1 (Fail)\n//Storyboard Layer 2 (Pass)\n//Storyboard Layer 3 (Foreground)\n//Storyboard Layer 4 (Overlay)\n//Storyboard Sound Samples\n\n[TimingPoints]\n0,352.941176470588,4,1,0,100,1,0\n\n\n[HitObjects]\n"

   for i in range(len(time)):
      osu = osu + str(int(bs[lineIndex[i]+13])*100) + ',' + str(int(bs[lineLayer[i]+13])*100) + ',' + str(convert(bpm, bs[(time[i]+8):(time[i]+24)])) + ',1,0,0:0:0:0:\n'


   with open(filenameosu, "w+") as myfile:
      myfile.write(osu)
      
   return(filenameosu + ' generated from ' + filenamedat)

print(difficulty('Normal', 5, 3.5, 6, 8, 1.4, 1))
print(difficulty('Hard', 5, 4.4, 8, 9, 2.5, 1))
print(difficulty('Expert', 5.5, 4.8, 8.5, 9, 3.2, 1))
print(difficulty('ExpertPlus', 5.6, 4.9, 8.6, 9, 3.3, 1))
print(difficulty('OneSaberNormal', 5, 3.5, 6, 8, 1.4, 1))
print(difficulty('OneSaberHard', 5, 4.4, 8, 9, 2.5, 1))
print(difficulty('OneSaberExpert', 5.5, 4.8, 8.5, 9, 3.2, 1))
print(difficulty('OneSaberExpertPlus', 5.6, 4.9, 8.6, 9, 3.3, 1))
print(difficulty('NoArrowsNormal', 5, 3.5, 6, 8, 1.4, 1))
print(difficulty('NoArrowsHard', 5, 4.4, 8, 9, 2.5, 1))
print(difficulty('NoArrowsExpert', 5.5, 4.8, 8.5, 9, 3.2, 1))
print(difficulty('NoArrowsExpertPlus', 5.6, 4.9, 8.6, 9, 3.3, 1))
print(difficulty('90DegreeNormal', 5, 3.5, 6, 8, 1.4, 1))
print(difficulty('90DegreeHard', 5, 4.4, 8, 9, 2.5, 1))
print(('90DegreeExpert', 5.5, 4.8, 8.5, 9, 3.2, 1))
print(difficulty('90DegreeExpertPlus', 5.6, 4.9, 8.6, 9, 3.3, 1))
print(difficulty('360DegreeNormal', 5, 3.5, 6, 8, 1.4, 1))
print(difficulty('360DegreeHard', 5, 4.4, 8, 9, 2.5, 1))
print(difficulty('360DegreeExpert', 5.5, 4.8, 8.5, 9, 3.2, 1))
print(difficulty('360DegreeExpertPlus', 5.6, 4.9, 8.6, 9, 3.3, 1))