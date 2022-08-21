# it needs to just not work when file exists
import os
if os.path.exists("generated.osu"):
    os.remove("generated.osu")

# open the file
fileosu = open("generated.osu", "x")
fileosu.close
# create string from file
with open('OneSaberHard.dat', 'r') as file:
    bs = file.read().replace('\n', '')
    
# creates what i think is lists? from stuffs
time = [i for i in range(len(bs)) if bs.startswith("_time", i)]
lineIndex = [i for i in range(len(bs)) if bs.startswith("_lineIndex", i)]
lineLayer = [i for i in range(len(bs)) if bs.startswith("_lineLayer", i)]
type = [i for i in range(len(bs)) if bs.startswith("_type", i)]
cutDirection = [i for i in range(len(bs)) if bs.startswith("_cutDirection", i)]

with open('Info.dat', 'r') as file:
    info = file.read().replace('\n', '')

ihatemyself=[i for i in range(len(info)) if info.startswith("_beatsPerMinute", i)]
bpm = (info[ihatemyself[0]+18:ihatemyself[0]+24])
bpm = bpm.replace(",", "")
bpm = bpm.strip()

# bpms = float(bpm)/60000
# print(bpms)
# the beginning of the osu file with dumb parameters but idk how to change them so circles are really slow and dumb and i dont like them
osu = "osu file format v14\n\n[General]\nAudioFilename: audio.mp3\nAudioLeadIn: 0\nPreviewTime: -1\nCountdown: 0\nSampleSet: Normal\nStackLeniency: 0.7\nMode: 0\nLetterboxInBreaks: 0\nWidescreenStoryboard: 0\n\n[Editor]\nDistanceSpacing: 1.1\nBeatDivisor: 4\nGridSize: 8\nTimelineZoom: 1.6\n\n[Metadata]\nTitle:generatedbeatmap\nTitleUnicode:generatedbeatmap\nArtist:beatmapgenerator\nArtistUnicode:beatmapgenerator\nCreator:beatmapgenerator\nVersion:Generated\nSource:\nTags:generated\nBeatmapID:0\nBeatmapSetID:-1\n\n[Difficulty]\nHPDrainRate:5\nCircleSize:5\nOverallDifficulty:5\nApproachRate:5\nSliderMultiplier:1.4\nSliderTickRate:1\n\n[Events]\n//Background and Video events\n//Break Periods\n//Storyboard Layer 0 (Background)\n//Storyboard Layer 1 (Fail)\n//Storyboard Layer 2 (Pass)\n//Storyboard Layer 3 (Foreground)\n//Storyboard Layer 4 (Overlay)\n//Storyboard Sound Samples\n\n[TimingPoints]\n0,352.941176470588,4,1,0,100,1,0\n\n\n[HitObjects]\n"

for i in range(len(time)):
   osu = osu + str(int(bs[lineIndex[i]+13])*100) + ',' + str(int(bs[lineLayer[i]+13])*100) + ',' + str(int(float(bs[time[i]+8:time[i]+16])*float(bpm))) + ',1,0,0:0:0:0:\n'

fileosu = open("generated.osu", "a")
fileosu.write(osu)
fileosu.close
# not sure what that one does...
