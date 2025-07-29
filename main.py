from morse_code import text_to_morse, morse_to_text

def main():
    text = input("Please enter your text:")
    _morse = text_to_morse(text)

    print(_morse)
    print("------------------------------")

    _text = morse_to_text(_morse)

    print("Here is the text: ")
    print(_text)

if __name__ == "__main__":
    main()
