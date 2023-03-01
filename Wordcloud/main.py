import phantom_tollbooth
import tollbooth_code


def main():
    book = phantom_tollbooth.get_text()
    tollbooth_code.count_words(book)
    tollbooth_code.organize_words()
    

if __name__ == '__main__':
    main()