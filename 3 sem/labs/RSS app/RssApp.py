import tkinter
import feedparser
import pyperclip
import string
import copy

import nltk
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

# nltk.download('averaged_perceptron_tagger')
# nltk.download('punkt')
# nltk.download('stopwords')

import pymorphy2



class RssApp:


    def __init__(self):


        # frames

        self.window = tkinter.Tk()

        self.enter_frame = tkinter.Frame(self.window)
        self.enter_frame.pack(side='left')

        self.text_frame = tkinter.Frame(self.window)
        self.text_frame.pack(side='left')

        self.user_preferences_frame = tkinter.Frame(self.window)
        self.user_preferences_frame.pack(side='left')

        # enter_frame subframes

        self.rss_frame = tkinter.Frame(self.enter_frame)
        self.rss_frame.pack()

        self.space_frame = tkinter.Frame(self.enter_frame)
        self.space_frame.pack()

        self.radio_frame = tkinter.Frame(self.enter_frame)
        self.radio_frame.pack()

        # text_frame subframes

        self.key_words_search_frame = tkinter.Frame(self.text_frame)
        self.key_words_search_frame.pack()

        self.space_frame_2 = tkinter.Frame(self.text_frame)
        self.space_frame_2.pack()

        self.listbox_frame = tkinter.Frame(self.text_frame)
        self.listbox_frame.pack()



        # variables for user preferences

        self.main_words_in_title = []
        self.main_words_in_title_counter = []
        self.most_often_appearing_words = []

        self.user_preferences_listbox_titles = []
        self.user_preferences_listbox_links = []


        # enter_frame elements

        # rss_frame elements begin
        self.entry_rss_link_label = tkinter.Label(
            self.rss_frame,
            text='Вставьте ссылку на RSS канал:'
        )
        self.entry_rss_link_label.pack()

        self.entry_rss_link = tkinter.Entry(
            self.rss_frame,
            width=30,
        )
        self.entry_rss_link.pack(side='left')

        self.rss_button = tkinter.Button(
            self.rss_frame,
            text='Перейти',
            command=self.entered_rss
        )
        self.rss_button.pack(side='left')

        self.space_1 = tkinter.Label(
            self.space_frame,
            text=''
        )
        self.space_1.pack()
        # rss_frame elements end

        # radio_frame elements begin
        self.listbox_of_news_field_label = tkinter.Label(
            self.radio_frame,
            text='Выберите тему:'
        )
        self.listbox_of_news_field_label.pack()

        self.listbox_of_news_field = tkinter.Listbox(
            self.radio_frame,
            height=12,
            width=20
        )
        self.listbox_of_news_field.pack()

        self.src_list = [
            'Новости', 'Статьи', 'Интервью', 'Фотоматериалы', 'Видеоматериалы', 'Политика', 'Экономика'
            , 'Общество', 'Мир', 'Спорт', 'Здоровье', 'Культура'
        ]
        for i in self.src_list:
            self.listbox_of_news_field.insert(tkinter.END, i)

        self.home_bd_go_to = tkinter.Button(
            self.radio_frame,
            text='Перейти',
            command=self.home_bd
        )
        self.home_bd_go_to.pack()

        self.space_2 = tkinter.Label(
            self.radio_frame,
            text=''
        )
        self.space_2.pack()
        # radio_frame elements end


        # text_frame elements begin

        # key_words_search_frame elements begin
        self.key_words_label = tkinter.Label(
            self.key_words_search_frame,
            text='Введите ключевые слова через запятую'
        )
        self.key_words_label.pack()

        self.key_words_entry = tkinter.Entry(
            self.key_words_search_frame,
            width=50
        )
        self.key_words_entry.pack()

        self.key_words_search_button = tkinter.Button(
            self.key_words_search_frame,
            text='Отфильтровать',
            command=self.search_by_key_words
        )
        self.key_words_search_button.pack()
        # key_words_search_frame elements end

        self.space_3 = tkinter.Label(
            self.space_frame_2,
            text=''
        )
        self.space_3.pack()

        # listbox_frame elements begin
        # listbox variables
        self.listbox_titles_backup = []
        self.listbox_links_backup = []
        self.listbox_titles = []
        self.listbox_links = []

        self.listbox = tkinter.Listbox(
            self.listbox_frame,
            height=20,
            width=100
        )
        self.listbox.pack()

        self.get_link_button = tkinter.Button(
            self.listbox_frame,
            text='Получить ссылку на статью',
            command=self.get_link
        )
        self.get_link_button.pack()
        # listbox_frame elements end


        # user_preferences_frame begin
        self.can_be_interesting_label = tkinter.Label(
            self.user_preferences_frame,
            text='Вам могут быть интересны:'
        )
        self.can_be_interesting_label.pack()

        self.user_preferences_listbox = tkinter.Listbox(
            self.user_preferences_frame,
            height=20,
            width=100
        )
        self.user_preferences_listbox.pack()
        # user_preferences_frame end

        # text_frame elements end


        self.window.mainloop()


    # methods

    def home_bd(self):
        rss_image = feedparser.parse(
            r'rss_bd\{0}.xml'.format(
                str(self.listbox_of_news_field.curselection()[0])
            )
        )
        for i in self.listbox_titles:
            self.listbox.delete(0)
        self.listbox_titles = []
        self.listbox_links = []
        for i in range(len(rss_image.entries)):
            self.listbox_titles.append(rss_image.entries[i]['title'])
            self.listbox_links.append(rss_image.entries[i]['link'])
        self.listbox_titles_backup = self.listbox_titles
        self.listbox_links_backup = self.listbox_links
        for i in self.listbox_titles:
            self.listbox.insert(tkinter.END, i)
        RssApp.proposals_for_user(self)


    def entered_rss(self):
        rss_image = feedparser.parse(self.entry_rss_link.get())
        for i in self.listbox_titles:
            self.listbox.delete(0)
        self.listbox_titles = []
        self.listbox_links = []
        for i in range(len(rss_image.entries)):
            self.listbox_titles.append(rss_image.entries[i]['title'])
            self.listbox_links.append(rss_image.entries[i]['link'])
        self.listbox_titles_backup = self.listbox_titles
        self.listbox_links_backup = self.listbox_links
        for i in self.listbox_titles:
            self.listbox.insert(tkinter.END, i)
        RssApp.proposals_for_user(self)


    def search_by_key_words(self):
        for i in self.listbox_titles:
            self.listbox.delete(0)
        self.listbox_titles = []
        self.listbox_links = []
        word_list = [
            i for i in nltk.word_tokenize(self.key_words_entry.get().lower()) if i not
            in string.punctuation and i not in stopwords.words('russian')
        ]
        if not word_list:
            word_list.append('')
        key_words = []
        stemmer = SnowballStemmer('russian')
        for i in word_list:
            key_words.append(stemmer.stem(i))
        for i in range(len(self.listbox_titles_backup)):
            for j in key_words:
                if self.listbox_titles_backup[i].lower().find(j) != -1:
                    self.listbox_titles.append(self.listbox_titles_backup[i])
                    self.listbox_links.append(self.listbox_links_backup[i])
                    break
        for i in self.listbox_titles:
            self.listbox.insert(tkinter.END, i)
        RssApp.proposals_for_user(self)


    def get_link(self):
        if self.user_preferences_listbox.curselection() != ():
            j = self.user_preferences_listbox.curselection()[0]
            pyperclip.copy(self.user_preferences_listbox_links[j])
        elif self.listbox.curselection() != ():
            j = self.listbox.curselection()[0]
            pyperclip.copy(self.listbox_links[j])
            title_of_current_article = self.listbox_titles[j].lower()
            key_words = []
            word_list = [
                i for i in nltk.word_tokenize(title_of_current_article) if
                i not in string.punctuation and i not in stopwords.words('russian')
            ]
            morph = pymorphy2.MorphAnalyzer()
            part_of_speech = [morph.parse(i)[0].tag.POS for i in word_list]
            for i in range(len(word_list)):
                if part_of_speech[i] == 'NOUN':
                    key_words.append(word_list[i])
                elif part_of_speech[i] == 'VERB':
                    key_words.append(word_list[i])
            for i in key_words:
                if i in self.main_words_in_title:
                    self.main_words_in_title_counter[self.main_words_in_title.index(i)] += 1
                else:
                    self.main_words_in_title.append(i)
                    self.main_words_in_title_counter.append(1)
            counter_copy = copy.deepcopy(self.main_words_in_title_counter)
            self.most_often_appearing_words = []
            if len(self.main_words_in_title_counter) <= 5:
                for i in range(len(self.main_words_in_title_counter)):
                    n = max(counter_copy)
                    ind = counter_copy.index(n)
                    counter_copy[ind] = 0
                    self.most_often_appearing_words.append(self.main_words_in_title[ind])
            else:
                for i in range(5):
                    n = max(counter_copy)
                    ind = counter_copy.index(n)
                    counter_copy[ind] = 0
                    self.most_often_appearing_words.append(self.main_words_in_title[ind])
            RssApp.proposals_for_user(self)


    def proposals_for_user(self):
        for i in self.user_preferences_listbox_titles:
            self.user_preferences_listbox.delete(0)
        self.user_preferences_listbox_titles = []
        self.user_preferences_listbox_links = []
        if not self.most_often_appearing_words:
            self.most_often_appearing_words.append('abrakada6ra')
        key_words = []
        stemmer = SnowballStemmer('russian')
        for i in self.most_often_appearing_words:
            key_words.append(stemmer.stem(i))
        for i in range(len(self.listbox_titles_backup)):
            for j in key_words:
                if self.listbox_titles_backup[i].lower().find(j) != -1:
                    self.user_preferences_listbox_titles.append(self.listbox_titles_backup[i])
                    self.user_preferences_listbox_links.append(self.listbox_links_backup[i])
                    break
        for i in self.user_preferences_listbox_titles:
            self.user_preferences_listbox.insert(tkinter.END, i)



t = RssApp()
