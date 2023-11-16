from notes.note import Note

class Actions:
    """
    Class for the Note Actions
    """
    def create(self, user: tuple):
        """
        Create a note in the database.
        """
        print(f'Ok {user[1]}, let\'s create a new note...')
        title = input('Note title: ')
        description = input('Note content: ')
        note = Note(user[0], title, description)
        save = note.save()
        if save[0] >= 1:
            print(f'You\'ve saved the note: {note.title}')
        else:
            print(f'The note has not been saved.')



    def show(self, user: tuple):
        """
        Show all user's notes.
        """
        print(f'ok {user[1]}, here are your notes...\n')
        note = Note(user[0])
        notes = note.show()
        for note in notes:
            print(f"""{'*'*40}
Note id: {note[0]}
Date: {note[4]}
Title: {note[2]}
Content: {note[3]}
""")

    def delete(self, user: tuple):
        """
        Delete a note from the user using the note title.
        """
        title = input('Enter the title of the note: ')
        note = Note(user_id=user[0])
        delete = note.delete(title)

        if delete[0] >= 1:
            print(f'The note \'{note.title}\' has been deleted.')
        else:
            print('There was an error. Please try again later.')