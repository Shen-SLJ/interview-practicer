from playsound import playsound
import gtts
import os
import random
import glob

if __name__ == '__main__':
    audio_ids = []

    # initialisation - generate audio
    regenerate = False
    if not os.path.exists("./audio"):
        os.mkdir("./audio")
        regenerate = True
    else:
        input = ("Regenerate audio (y/n)?")
        if input.lower() == "y":
            for path in glob.glob("./audio/*"):
                os.remove(path)
            os.rmdir("./audio")
            regenerate = True
    if regenerate:
        f = open("questions.txt", "r")
        lines = f.read().splitlines()
        for i, line in enumerate(lines):
            tts = gtts.gTTS(line, tld="fr") # an object
            tts.save(f"./audio/audio{i}.mp3")
            audio_ids.append(i)
        f.close()

    # play audio
    while len(audio_ids) > 0:
        input("Press enter to proceed.")
        rand_i = random.randint(0, len(audio_ids)-1)
        playsound(f"./audio/audio{audio_ids[rand_i]}.mp3")
        del audio_ids[rand_i]