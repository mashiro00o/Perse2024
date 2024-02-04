story_words = []

while True:
    word = input()
    if word.lower() == 'stop':
        break
    else:
        story_words.append(word)
joint_story = ' '.join(story_words)

# main
print(joint_story)
