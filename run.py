from playsound import playsound
import gtts
import os
import random
import glob

if __name__ == '__main__':
    audio_ids = []

    # initialisation - determine load from previous audio/generate new audio
    regenerate = False
    if not os.path.exists("./audio"):
        os.mkdir("./audio")
        regenerate = True
    else:
        ans = input("Regenerate audio (y/n)? ")
        if ans.lower() == "y":
            for path in glob.glob("./audio/*"):
                os.remove(path)
            regenerate = True
        else:
            try:
                audio_ids_f = open("ids.txt", "r")
                str_ids = audio_ids_f.read().splitlines()
                audio_ids = [int(id) for id in str_ids]
            except FileNotFoundError:
                print("ids.txt file is missing.")
                regenerate = True # need to regenerate if no id file

    if regenerate:
        print("Generating audio. Please wait.")

        # generate audio files
        f = open("questions.txt", "r")
        lines = f.read().splitlines()
        for i, line in enumerate(lines):
            tts = gtts.gTTS(line, tld="fr") # an object
            tts.save(f"./audio/audio{i}.mp3")
            audio_ids.append(i)
        f.close()

        # write for potential next time loading
        id_store = open("ids.txt", "w")
        for id in audio_ids:
            id_store.write(f"{id}\n")

    # play audio
    while len(audio_ids) > 0:
        input("Press enter to proceed.")
        rand_i = random.randint(0, len(audio_ids)-1)
        playsound(f"./audio/audio{audio_ids[rand_i]}.mp3")
        del audio_ids[rand_i]