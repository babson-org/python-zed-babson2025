def text_analysis():
    """
    Ask the user for a block of text.
    Count and display:
        - Number of letters (only count a-zA-Z)
        - Number of words   (use split())
        - Number of sentences (., ?, !) 
    """

    print("you have some work todo!, text_analysis")

    # TODO: Get user input
    text = input("Enter some text: ")

    # TODO: Count letters
    letters = 0
    for let in text:
        if let.isalpha():
            letters += 1

    # TODO: Count words
    word_list = text.split()
    word = len(word_list)
    # TODO: Count sentences
    sentences = 0
    for let in text:
     if let == '.' or let == '!' or let == '?':
        sentences += 1
    # TODO: Print the results
    print(f"Letters: {letters}")
    print(f"Words: {1}")        # replace 0
    print(f"Sentences: {1}")    # replace 0

# Uncomment to test Part 2
text_analysis()