import datetime

def info():
    print("""The current APA completion function support:
1. course material
2. web pages
3. newspaper
4. datasets
5. tables
6. Journal
    1. Electronic Journal
    2. Printed Journal
    3. Magazine
    4. Secondary Source
Please check the reference followed the University of Melbourne APA 7 website
""")

def Year(class_year, year):
    class_year.year = str(year)

def Authors(class_author, Authors):
    names = list(Authors)
    str_name = []
    for author in names:
        if len(author.split(' ')) == 2:
             first, last = author.split(' ')
             name = first.title() + ', ' + last.title()[0] + '.'
             str_name.append(name)
        elif len(author.split(' ')) == 3:
             first, middle, last = author.split(' ')
             name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
             str_name.append(name)
        else:
             str_name.append(author + '. ')
    
    names = ''
    if len(str_name) > 1:
        for name in str_name:
            if str_name[-1] != name:
                names += name + ' '
            else:
                names += '& ' + name
    else:
        names = str_name[0]
    
    class_author.author = names

def dump(Obj, filename):
    output_file = open(filename, 'a')
    output_file.write("========================================<br>")
    output_file.write(str(datetime.datetime.now()))
    output_file.write('<br> Reference: <br>')
    output_file.write(Obj.reference)
    output_file.write('<br> In text 1: <br>')
    output_file.write(Obj.in_text)
    output_file.write('<br> In text 2: <br>')
    output_file.write(Obj.intext)
    output_file.write('<br>')
    output_file.write("========================================<br>")

class course_material:
    def __init__(self, author = '', year = '', title = '', url = ''):
        self.author = author
        self.year = year
        self.title = title
        self.url = url
        self.short_ref = ''
        self.intext = ''
        self.in_text = ''
        self.reference = ''
        self.info()
        
    def Author(self, authors):
        str_name = []
        for author in authors:
            if len(author.split(' ')) == 2:
                first, last = author.split(' ')
                name = first.title() + ', ' + last.title()[0] + '.'
                str_name.append(name)
            elif len(author.split(' ')) == 3:
                first, middle, last = author.split(' ')
                name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                str_name.append(name)
            else:
                str_name.append(author + '. ')
        name = ' '.join(str_name)
        self.author = name     
 
        name = authors[0]
        if len(name.split(' ')) == 2:
            first, last = name.split(' ')
            name = first.title() + ', ' + last.title()[0] + '.'
        elif len(name.split(' ')) == 3:
            first, middle, last = name.split(' ')
            name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
        else:
            name = name.split(' ')[0]
            
        if len(authors) > 3:
            self.short_ref = name + ' et al.'
        else:
            self.short_ref = self.author
        
        self.info()
    
    def info(self):
        print("  ____                            __  __       _            _       _")
        print(" / ___|___  _   _ _ __ ___  ___  |  \/  | __ _| |_ ___ _ __(_) __ _| |")
        print("| |   / _ \| | | | '__/ __|/ _ \ | |\/| |/ _` | __/ _ \ '__| |/ _` | |")
        print("| |__| (_) | |_| | |  \__ \  __/ | |  | | (_| | ||  __/ |  | | (_| | |")
        print(" \____\___/ \__,_|_|  |___/\___| |_|  |_|\__,_|\__\___|_|  |_|\__,_|_|")
        print("======================================================================")
        print("Current course material has information")
        print("======================================================================")
        print(f"Author name        :: {self.author}")
        print(f"year               :: {self.year}")
        print(f"Presentation title :: {self.title}")
        print(f"URL                :: {self.url}")
        print(f"In text citation 1 :: {self.intext}")
        print(f"In text citation 2 :: {self.in_text}")
        print(f"Reference          :: {self.reference}")
        print("======================================================================")

    def Year(self, year):
        self.year = f"{year}"
        
    def Title(self, title):
        self.title = title + '. '
        
    def Url(self, url):
        self.url = url

    def ref(self):
        reference = self.author + ' (' + self.year + '). ' + self.title + self.url
        self.reference = reference
        self.in_text = '(' + self.short_ref + ', ' + self.year + ')'
        self.intext = self.short_ref + f" ({self.year})"
        
        print('\n\n\n')
        print("======================================================================")
        print('The completed reference is :: ')
        print("======================================================================")
        print(self.reference)
        print("======================================================================")
        print('In text citation 1 :: ')
        print(self.in_text)
        print("======================================================================")
        print('In text citation 2 :: ')
        print(self.intext)
        print("======================================================================")
        print('\n\n\n')  

class webpages:
    def __init__(self, author = '', date = '', title_of_page = '', website_name = '', url = ''):
        self.author = author
        self.date = date
        self.title = title_of_page
        self.name = website_name
        self.url = url
        self.intext = ''
        self.in_text = ''
        self.reference = ''
        self.info()
        
    def info(self):
        print("__        __   _     ____")
        print("\ \      / /__| |__ |  _ \ __ _  __ _  ___  ___")
        print(" \ \ /\ / / _ \ '_ \| |_) / _` |/ _` |/ _ \/ __|")
        print("  \ V  V /  __/ |_) |  __/ (_| | (_| |  __/\__ \\")
        print("   \_/\_/ \___|_.__/|_|   \__,_|\__, |\___||___/")
        print("                                |___/")
        print("======================================================================")
        print("Current webpages has information")
        print("======================================================================")
        print(f"Author name        :: {self.author}")
        print(f"Date               :: {self.date}   // Please check the date follow the format (Year, Month 11 format or Year only)")
        print(f"Title of page      :: {self.title}")
        print(f"Website name       :: {self.name}")
        print(f"URL                :: {self.url}")
        print(f"In text citation 1 :: {self.intext}")
        print(f"In text citation 2 :: {self.in_text}")
        print(f"Reference          :: {self.reference}")
        print("======================================================================")
        
    def Author(self, authors):
        str_name = []
        for author in authors:
            if len(author.split(' ')) == 2:
                first, last = author.split(' ')
                name = first.title() + ', ' + last.title()[0] + '.'
                str_name.append(name)
            elif len(author.split(' ')) == 3:
                first, middle, last = author.split(' ')
                name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                str_name.append(name)
            else:
                str_name.append(author + '. ')
        name = ' '.join(str_name)
        self.author = name  

    def Date(self, date):
        self.date = date
        
    def Title(self, title):
        self.title = title
    
    def Url(self, url):
        self.url = url
    
    def Name(self, webpage_name):
        self.name = webpage_name
    
    def ref(self):
        name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
        name = ' '.join(name)
        if self.author != '':
            reference = f"{self.author} ({self.date}). <i>{self.title}</i>. {self.name}. {self.url}"
            if len(name.split(' ')) > 4:
                intext = f"({self.author.split('.')[0]} et al., {self.date})"
                in_text = f"{self.author.split('.')[0]} et al. ({self.date})"
            else:
                intext = f"({self.author}, {self.date})"
                in_text = f"{self.author} ({self.date})"
        else:
            reference = f" {self.name} ({self.date}). <i>{self.title}</i>. {self.url}"
            intext = f"{name} ({self.date})"
            in_text = f"({name}, {self.date})"
        self.reference = reference
        self.intext = intext
        self.in_text = in_text
        self.info()

class newspaper:
    def __init__(self, author='', title = '', year='', month='', day='', publication='', source=''):
        self.author = author
        self.title = title
        self.year = year
        self.month = month
        self.day = day
        self.publication = publication
        self.source = source
        self.intext = ''
        self.in_text = ''
        self.reference = ''
        self.info()
    
    def info(self):
        print(" _   _                   ____")
        print("| \ | | _____      _____|  _ \ __ _ _ __   ___ _ __ ___")
        print("|  \| |/ _ \ \ /\ / / __| |_) / _` | '_ \ / _ \ '__/ __|")
        print("| |\  |  __/\ V  V /\__ \  __/ (_| | |_) |  __/ |  \__ \\")
        print("|_| \_|\___| \_/\_/ |___/_|   \__,_| .__/ \___|_|  |___/")
        print("                                   |_|")
        print("======================================================================")
        print("Current course material has information")
        print("======================================================================")
        print(f"Author name        :: {self.author}")
        print(f"Title              :: {self.title}")
        print(f"Year               :: {self.year}")
        print(f"Month              :: {self.month}")
        print(f"Day                :: {self.day}")
        print(f"Publication name   :: {self.publication}")
        print(f"Source             :: {self.source}")
        print(f"In text citation 1 :: {self.intext}")
        print(f"In text citation 2 :: {self.in_text}")
        print(f"Reference          :: {self.reference}")
        print("======================================================================")
        
    def Author(self, authors):
         str_name = []
         for author in authors:
             if len(author.split(' ')) == 2:
                 first, last = author.split(' ')
                 name = first.title() + ', ' + last.title()[0] + '.'
                 str_name.append(name)
             elif len(author.split(' ')) == 3:
                 first, middle, last = author.split(' ')
                 name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                 str_name.append(name)
             else:
                 str_name.append(author + '. ')
         name = ' '.join(str_name)
         self.author = name   

    def Year(self, year):
        self.year = year
    
    def Month(self, month):
        self.month = month
        
    def Day(self, day):
        self.day = day
        
    def Public(self, publication):
        self.publication = publication
    
    def Source(self, source):
        self.source = source
        
    def ref(self):
        name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
        name = ' '.join(name)
        if self.author == '':
            reference = f"{self.title}. ({self.year}, {self.month} {self.day}). <i>{self.publication}</i>. {self.source}"
            intext = f"({self.title} {self.year})"
            in_text = f"{self.title}, ({self.year})"
        else:
            reference = f"{self.author} ({self.year}, {self.month} {self.day}). {self.title}. <i>{self.publication}</i>. {self.source}"
            if len(name.split(' ')) > 4:
                intext = f"({self.author.split('.')[0]} et al., ({self.year}, {self.month} {self.day})"
                in_text = f"{self.author.split('.')[0]} et al. ({self.year}, {self.month} {self.day})"
            else:
                intext = f"({name}, {self.year})"
                in_text = f"{name} ({self.year})"
        self.reference = reference
        self.intext = intext
        self.in_text = in_text
        self.info()
    
    def Title(self, title):
        self.title = title
        
class datasets:
    def __init__(self, author='', year='', title_of_data='', publication='', url=''):
        self.author = author
        self.year = year
        self.title = title_of_data
        self.publication = publication
        self.source = url
        self.intext = ''
        self.in_text = ''
        self.reference = ''
        self.info()
    
    def info(self):
        print(" ____        _        ____       _")
        print("|  _ \  __ _| |_ __ _/ ___|  ___| |_ ___")
        print("| | | |/ _` | __/ _` \___ \ / _ \ __/ __|")
        print("| |_| | (_| | || (_| |___) |  __/ |_\__ \\")
        print("|____/ \__,_|\__\__,_|____/ \___|\__|___/")
        print("======================================================================")
        print("Current course material has information")
        print("======================================================================")
        print(f"Author name        :: {self.author}")
        print(f"Year               :: {self.year}")
        print(f"Title of data set  :: {self.title}")
        print(f"Publication name   :: {self.publication}")
        print(f"Source             :: {self.source}")
        print(f"In text citation 1 :: {self.intext}")
        print(f"In text citation 2 :: {self.in_text}")
        print(f"Reference          :: {self.reference}")
        print("======================================================================")
    
    def Author(self, Authors):
        names = list(Authors)
        str_name = []
        for author in names:
            if len(author.split(' ')) == 2:
                 first, last = author.split(' ')
                 name = first.title() + ', ' + last.title()[0] + '.'
                 str_name.append(name)
            elif len(author.split(' ')) == 3:
                 first, middle, last = author.split(' ')
                 name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                 str_name.append(name)
            else:
                 str_name.append(author + '. ')
        
        names = ''
        if len(str_name) > 1:
            for name in str_name:
                if str_name[-1] != name:
                    names += name + ' '
                else:
                    names += '& ' + name
        else:
            names = str_name[0]
        
        self.author = names
    
    def Public(self, publication):
        self.publication = publication
    
    def Year(self, year):
        self.year = year
    
    def Title(self, title):
        self.title = title
        
    def Source(self, url):
        self.url = url
        
    def ref(self):
        name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
        name = ' '.join(name)
        reference = f"{name} ({self.year}). <i>{self.title}</i> [Data set]. {self.publication}. {self.source}"
        self.reference = reference
        if len(name.split(' ')) > 4:
            intext = f"({self.author.split('.')[0]} et al., ({self.year})"
            in_text = f"{self.author.split('.')[0]} et al. ({self.year})"
        else:
            intext = f"({name}, {self.year})"
            in_text = f"{name} ({self.year})"
        self.intext = intext
        self.in_text = in_text
        self.info()

class tables:
    def __init__(self, title='', author='', year = '', publisher='', url = '', copyright = '', year_copyright=''):
        self.author = author
        self.title = title
        self.publisher = publisher
        self.year = year
        self.copyright = copyright
        self.year_copyright = year_copyright
        self.reference = ''
        self.intext = ''
        self.in_text = ''
        self.source = url
        self.info()
    
    def info(self):
        print(" _____     _     _")
        print("|_   _|_ _| |__ | | ___  ___")
        print("  | |/ _` | '_ \| |/ _ \/ __|")
        print("  | | (_| | |_) | |  __/\__ \\")
        print("  |_|\__,_|_.__/|_|\___||___/")
        print("======================================================================")
        print("Current course material has information")
        print("======================================================================")
        print(f"Title of tables    :: {self.title}")
        print(f"Author name        :: {self.author}")
        print(f"Year               :: {self.year}")
        print(f"Publisher          :: {self.publisher}")
        print(f"Source             :: {self.source}")
        print(f"Copyright          :: {self.copyright}")
        print(f"Year of Copyright  :: {self.year_copyright}")
        print(f"Reference          :: {self.reference}")        
        print("======================================================================")
        
    def Author(self, Authors):
        names = list(Authors)
        str_name = []
        for author in names:
            if len(author.split(' ')) == 2:
                 first, last = author.split(' ')
                 name = first.title() + ', ' + last.title()[0] + '.'
                 str_name.append(name)
            elif len(author.split(' ')) == 3:
                 first, middle, last = author.split(' ')
                 name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                 str_name.append(name)
            else:
                 str_name.append(author + '. ')
        
        names = ''
        if len(str_name) > 1:
            for name in str_name:
                if str_name[-1] != name:
                    names += name + ' '
                else:
                    names += '& ' + name
        else:
            names = str_name[0]
        
        self.author = names
        self.info()   
        
    def Publisher(self, publisher):
        self.publisher = publisher
        
    def Title(self, title):
        self.title = title
    
    def Copyright(self, copyright):
        self.copyright = copyright
    
    def Year_copyright(self, year):
        self.year_copyright = year
    
    def Year(self, year):
        self.year = year
    
    def Source(self, url):
        self.source = url
    
    def ref(self):
        name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
        name = ' '.join(name)
        reference = f"<i>Note</i>. From <i>{self.title}</i> by {name},{self.year},{self.publisher}, {self.source}. Copyright {self.year_copyright} by {self.copyright}."
        self.reference = reference

class journal_and_magazine:
    class electronic_journal:
        def __init__(self, author='', publication_date='', title_of_article='', title_of_publication='', volume_number='', issue_number = '', page_range='', url=''):
            self.author = author
            self.date = publication_date
            self.title_article = title_of_article
            self.title_publication = title_of_publication
            self.volume = volume_number
            self.issue = issue_number
            self.prange = page_range
            self.source = url
            self.in_text = ''
            self.intext = ''
            self.reference = ''
            self.info()
            
        def info(self):
            print(" _____               _                              _")
            print("| ____|             | | ___  _   _ _ __ _ __   __ _| |")
            print("|  _|    _____   _  | |/ _ \| | | | '__| '_ \ / _` | |")
            print("| |___  |_____| | |_| | (_) | |_| | |  | | | | (_| | |")
            print("|_____|          \___/ \___/ \__,_|_|  |_| |_|\__,_|_|")
            print("======================================================================")
            print("Current course material has information")
            print("======================================================================")
            print(f"Author name        :: {self.author}")
            print(f"Publication Date   :: {self.date}")
            print(f"Title of article   :: {self.title_article}")
            print(f"Title of publisher :: {self.title_publication}")
            print(f"Volume number      :: {self.volume}")
            print(f"Issue number       :: {self.issue}")
            print(f"Page range         :: {self.prange}")
            print(f"Source             :: {self.source}")
            print(f"In text citation 1 :: {self.intext}")
            print(f"In text citation 2 :: {self.in_text}")
            print(f"Reference          :: {self.reference}")        
            print("======================================================================")
            
        def Author(self, Authors):
            names = list(Authors)
            str_name = []
            for author in names:
                if len(author.split(' ')) == 2:
                     first, last = author.split(' ')
                     name = first.title() + ', ' + last.title()[0] + '.'
                     str_name.append(name)
                elif len(author.split(' ')) == 3:
                     first, middle, last = author.split(' ')
                     name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                     str_name.append(name)
                else:
                     str_name.append(author + '. ')
            
            names = ''
            if len(str_name) > 1:
                for name in str_name:
                    if str_name[-1] != name:
                        names += name + ' '
                    else:
                        names += '& ' + name
            else:
                names = str_name[0]
            
            self.author = names
            self.info()  
            
        def Date(self, date):
            self.date = date
        
        def T_article(self, title):
            self.title_article = title
        
        def T_publication(self, title):
            self.title_publication = title
        
        def Volume(self, volume):
            self.volume = volume

        def Page_range(self, prange):
            self.prange = prange
        
        def Source(self, source):
            self.source = source
        
        def Issue(self, num):
            self.issue = num
        
        def ref(self):
            reference = f"{self.author} ({self.date}). {self.title_article}. <i>{self.title_publication}, {self.volume}</i>({self.issue}). {self.prange}. {self.source}"
            self.reference = reference
            name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
            name = ' '.join(name)
            if len(name.split(' ')) > 4:
                intext = f"({self.author.split('.')[0]} et al., ({self.date})"
                in_text = f"{self.author.split('.')[0]} et al. ({self.date})"
            else:
                intext = f"({name}, {self.date})"
                in_text = f"{name} ({self.date})"
            self.intext = intext
            self.in_text = in_text
            self.info()
            
    class printed_journal:
        def __init__(self, author='', publication_date='', title_of_article='', title_of_publication='', volume_number='', issue_number = '', page_range='', url=''):
            self.author = author
            self.date = publication_date
            self.title_article = title_of_article
            self.title_publication = title_of_publication
            self.volume = volume_number
            self.issue = issue_number
            self.prange = page_range
            self.in_text = ''
            self.intext = ''
            self.reference = ''
            self.info()
            
        def info(self):
            print(" ____       _       _           _       _                              _")
            print("|  _ \ _ __(_)_ __ | |_ ___  __| |     | | ___  _   _ _ __ _ __   __ _| |")
            print("| |_) | '__| | '_ \| __/ _ \/ _` |  _  | |/ _ \| | | | '__| '_ \ / _` | |")
            print("|  __/| |  | | | | | ||  __/ (_| | | |_| | (_) | |_| | |  | | | | (_| | |")
            print("|_|   |_|  |_|_| |_|\__\___|\__,_|  \___/ \___/ \__,_|_|  |_| |_|\__,_|_|")
            print("======================================================================")
            print("Current course material has information")
            print("======================================================================")
            print(f"Author name        :: {self.author}")
            print(f"Publication Date   :: {self.date}")
            print(f"Title of article   :: {self.title_article}")
            print(f"Title of publisher :: {self.title_publication}")
            print(f"Volume number      :: {self.volume}")
            print(f"Issue number       :: {self.issue}")
            print(f"Page range         :: {self.prange}")
            print(f"In text citation 1 :: {self.intext}")
            print(f"In text citation 2 :: {self.in_text}")
            print(f"Reference          :: {self.reference}")        
            print("======================================================================")
            
        def Author(self, Authors):
            names = list(Authors)
            str_name = []
            for author in names:
                if len(author.split(' ')) == 2:
                     first, last = author.split(' ')
                     name = first.title() + ', ' + last.title()[0] + '.'
                     str_name.append(name)
                elif len(author.split(' ')) == 3:
                     first, middle, last = author.split(' ')
                     name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                     str_name.append(name)
                else:
                     str_name.append(author + '. ')
            
            names = ''
            if len(str_name) > 1:
                for name in str_name:
                    if str_name[-1] != name:
                        names += name + ' '
                    else:
                        names += '& ' + name
            else:
                names = str_name[0]
            
            self.author = names
            self.info()  
            
        def Date(self, date):
            self.date = date
        
        def T_article(self, title):
            self.title_article = title
        
        def T_publication(self, title):
            self.title_publication = title
        
        def Volume(self, volume):
            self.volume = volume

        def Page_range(self, prange):
            self.prange = prange
        
        def Issue(self, num):
            self.issue = num
        
        def ref(self):
            reference = f"{self.author} ({self.date}). {self.title_article}. <i>{self.title_publication}, {self.volume}</i>({self.issue}). {self.prange}."
            self.reference = reference
            name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
            name = ' '.join(name)
            if len(name.split(' ')) > 4:
                intext = f"({self.author.split('.')[0]} et al., ({self.date})"
                in_text = f"{self.author.split('.')[0]} et al. ({self.date})"
            else:
                intext = f"({name}, {self.date})"
                in_text = f"{name} ({self.date})"
            self.intext = intext
            self.in_text = in_text
            self.info()
    
    class magazine:
        def __init__(self, author='', year = '', month = '', day = '', title_of_article='', title_of_publication='', volume_number='', issue_number = '', page_range='', url=''):
            self.author = author
            self.date = ''
            self.year = year
            self.month = month
            self.day = day
            self.title_article = title_of_article
            self.title_publication = title_of_publication
            self.volume = volume_number
            self.issue = issue_number
            self.prange = page_range
            self.in_text = ''
            self.intext = ''
            self.reference = ''
            self.info()
            
        def info(self):
            print(" __  __                 _")
            print("|  \/  | __ _  __ _ ___(_)_ __   ___")
            print("| |\/| |/ _` |/ _` |_  / | '_ \ / _ \\")
            print("| |  | | (_| | (_| |/ /| | | | |  __/")
            print("|_|  |_|\__,_|\__, /___|_|_| |_|\___|")
            print("              |___/")
            print("======================================================================")
            print("Current course material has information")
            print("======================================================================")
            print(f"Author name        :: {self.author}")
            print(f"Year               :: {self.year}")
            print(f"Month              :: {self.month}")
            print(f"Day                :: {self.day}")
            print(f"Title of article   :: {self.title_article}")
            print(f"Title of publisher :: {self.title_publication}")
            print(f"Volume number      :: {self.volume}")
            print(f"Issue number       :: {self.issue}")
            print(f"Page range         :: {self.prange}")
            print(f"In text citation 1 :: {self.intext}")
            print(f"In text citation 2 :: {self.in_text}")
            print(f"Reference          :: {self.reference}")        
            print("======================================================================")
            
        def Author(self, Authors):
            names = list(Authors)
            str_name = []
            for author in names:
                if len(author.split(' ')) == 2:
                     first, last = author.split(' ')
                     name = first.title() + ', ' + last.title()[0] + '.'
                     str_name.append(name)
                elif len(author.split(' ')) == 3:
                     first, middle, last = author.split(' ')
                     name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                     str_name.append(name)
                else:
                     str_name.append(author + '. ')
            
            names = ''
            if len(str_name) > 1:
                for name in str_name:
                    if str_name[-1] != name:
                        names += name + ' '
                    else:
                        names += '& ' + name
            else:
                names = str_name[0]
            
            self.author = names
            self.info()  
            
        def Year(self, year):
            self.year = year
        
        def Month(self, month):
            self.month = month
            
        def Day(self, day):
            self.day = day
        
        def T_article(self, title):
            self.title_article = title
        
        def T_publication(self, title):
            self.title_publication = title
        
        def Volume(self, volume):
            self.volume = volume

        def Page_range(self, prange):
            self.prange = prange
        
        def Issue(self, num):
            self.issue = num
        
        def ref(self):
            self.date = f"{self.year}, {self.month} {self.day}"
            reference = f"{self.author} ({self.date}). {self.title_article}. <i>{self.title_publication}, {self.volume}</i>({self.issue}). {self.prange}."
            self.reference = reference
            name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
            name = ' '.join(name)
            if len(name.split(' ')) > 3:
                intext = f"({self.author.split('.')[0]} et al., ({self.year})"
                in_text = f"{self.author.split('.')[0]} et al. ({self.year})"
            else:
                intext = f"({name}, {self.year})"
                in_text = f"{name} ({self.year})"
            self.intext = intext
            self.in_text = in_text
            self.info()
        
    class secondary_source:
        def __init__(self, author='', author_of_article = '', year = '', title_of_article='', name_of_journal='', volume_number='', issue_number = '', page_range='', url=''):
            self.author = author
            self.author_article = author_of_article
            self.year = year
            self.title_article = title_of_article
            self.journal_name = name_of_journal
            self.volume = volume_number
            self.issue = issue_number
            self.prange = page_range
            self.source = url
            self.in_text = ''
            self.intext = ''
            self.reference = ''
            self.info()
            
        def info(self):
            print(" ____                           _")
            print("/ ___|  ___  ___ ___  _ __   __| | __ _ _ __ _   _")
            print("\___ \ / _ \/ __/ _ \| '_ \ / _` |/ _` | '__| | | |")
            print(" ___) |  __/ (_| (_) | | | | (_| | (_| | |  | |_| |")
            print("|____/ \___|\___\___/|_| |_|\__,_|\__,_|_|   \__, |")
            print("                                             |___/")
            print("======================================================================")
            print("Current course material has information")
            print("======================================================================")
            print(f"Author name        :: {self.author}")
            print(f"Author of article  :: {self.author_article}")
            print(f"Year               :: {self.year}")
            print(f"Title of article   :: {self.title_article}")
            print(f"Name of the journal:: {self.journal_name}")
            print(f"Volume number      :: {self.volume}")
            print(f"Issue number       :: {self.issue}")
            print(f"Page range         :: {self.prange}")
            print(f"Source             :: {self.source}")
            print(f"In text citation 1 :: {self.intext}")
            print(f"In text citation 2 :: {self.in_text}")
            print(f"Reference          :: {self.reference}")        
            print("======================================================================")
            
        def Author(self, Authors):
            names = list(Authors)
            str_name = []
            for author in names:
                if len(author.split(' ')) == 2:
                     first, last = author.split(' ')
                     name = first.title() + ', ' + last.title()[0] + '.'
                     str_name.append(name)
                elif len(author.split(' ')) == 3:
                     first, middle, last = author.split(' ')
                     name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                     str_name.append(name)
                else:
                     str_name.append(author + '. ')
            
            names = ''
            if len(str_name) > 1:
                for name in str_name:
                    if str_name[-1] != name:
                        names += name + ' '
                    else:
                        names += '& ' + name
            else:
                names = str_name[0]
            
            self.author = names
            
        def Year(self, year):
            self.year = year
        
        def Author_article(self, Authors):
            names = list(Authors)
            str_name = []
            for author in names:
                if len(author.split(' ')) == 2:
                     first, last = author.split(' ')
                     name = first.title() + ', ' + last.title()[0] + '.'
                     str_name.append(name)
                elif len(author.split(' ')) == 3:
                     first, middle, last = author.split(' ')
                     name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                     str_name.append(name)
                else:
                     str_name.append(author + '. ')
            
            names = ''
            if len(str_name) > 1:
                for name in str_name:
                    if str_name[-1] != name:
                        names += name + ' '
                    else:
                        names += '& ' + name
            else:
                names = str_name[0]
            
            self.author_article = names
        
        def T_article(self, title):
            self.title_article = title
        
        def Name_journal(self, name):
            self.journal_name = name
        
        def Volume(self, volume):
            self.volume = volume

        def Page_range(self, prange):
            self.prange = prange
        
        def Issue(self, num):
            self.issue = num
        
        def ref(self):
            if self.author_article == '':
                reference = f"{self.author} ({self.year}). {self.title_article}. <i>{self.journal_name}, {self.volume}</i>({self.issue}). {self.prange}. {self.source}"
            else:
                reference = f"{self.author} [{self.author_article}] ({self.year}). {self.title_article}. <i>{self.journal_name}, {self.volume}</i>({self.issue}). {self.prange}. {self.source}"
            self.reference = reference
            name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
            name = ' '.join(name)
            if len(name.split(' ')) > 4:
                intext = f"({self.author.split('.')[0]} et al. as cited in {self.author_article}, ({self.year})"
                in_text = f"{self.author.split('.')[0]} et al as cited in {self.author_article}. ({self.year})"
            else:
                intext = f"({name} as cited in {self.author_article}, {self.year})"
                in_text = f"{name} (as cited in {self.author_article}, {self.year})"
            self.intext = intext
            self.in_text = in_text
            self.info()
        
class books:
    class book:
        def __init__(self, author = '', year = '', title = '', publisher = ''):
            self.author = author
            self.year = year
            self.title = title
            self.publisher = ''
            self.intext = ''
            self.in_text = ''
            self.intext = ''
            self.reference = ''
            self.info()
        
        def info(self):
            print(" ____              _")
            print("| __ )  ___   ___ | | __")
            print("|  _ \ / _ \ / _ \| |/ /")
            print("| |_) | (_) | (_) |   <")
            print("|____/ \___/ \___/|_|\_\\")
            print("======================================================================")
            print("Current course material has information")
            print("======================================================================")
            print(f"Author name        :: {self.author}")
            print(f"Year               :: {self.year}")
            print(f"Title of Book      :: {self.title}")
            print(f"Publisher          :: {self.publisher}")
            print(f"In text citation 1 :: {self.intext}")
            print(f"In text citation 2 :: {self.in_text}")
            print(f"Reference          :: {self.reference}")        
            print("======================================================================")
           
        def Authors(self, Authors):
            names = list(Authors)
            str_name = []
            for author in names:
                if len(author.split(' ')) == 2:
                     first, last = author.split(' ')
                     name = first.title() + ', ' + last.title()[0] + '.'
                     str_name.append(name)
                elif len(author.split(' ')) == 3:
                     first, middle, last = author.split(' ')
                     name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                     str_name.append(name)
                else:
                     str_name.append(author + '. ')
            
            names = ''
            if len(str_name) > 1:
                for name in str_name:
                    if str_name[-1] != name:
                        names += name + ' '
                    else:
                        names += '& ' + name
            else:
                names = str_name[0]
            
            self.author = names
           
        def Title(self, title):
            self.title = title
        
        def Year(self, year):
            self.year = year
            
        def Publisher(self, publisher):
            self.publisher = publisher
 
        def ref(self):
            reference = f"{self.author} ({self.year}). <i>{self.title}</i>. {self.publisher}"         
            name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
            name = ' '.join(name)
            if len(name.split(' ')) > 4:
                intext = f"({name.split(' ')[0]} et al. ({self.year})"
                in_text = f"{name.split(' ')[0]} et al. ({self.year})"
            else:
                intext = f"({name}, {self.year})"
                in_text = f"{name}, {self.year})"
            self.intext = intext
            self.in_text = in_text
            self.reference = reference
            self.info()
            
    class book_chapter:
        def __init__(self, author='', year='', title_chapter='', editor='', title_book='', page_range='', publisher=''):
            self.author = author
            self.year = year
            self.title_chapter = title_chapter
            self.editor = editor
            self.title_book = title_book
            self.prange = page_range
            self.publisher = ''
            self.intext = ''
            self.in_text = ''
            self.intext = ''
            self.reference = ''
            self.info()
        
        def info(self):
            print(" ____              _       ____ _                 _")
            print("| __ )  ___   ___ | | __  / ___| |__   __ _ _ __ | |_ ___ _ __")
            print("|  _ \ / _ \ / _ \| |/ / | |   | '_ \ / _` | '_ \| __/ _ \ '__|")
            print("| |_) | (_) | (_) |   <  | |___| | | | (_| | |_) | ||  __/ |")
            print("|____/ \___/ \___/|_|\_\  \____|_| |_|\__,_| .__/ \__\___|_|")
            print("                                           |_|")
            print("======================================================================")
            print("Current course material has information")
            print("======================================================================")
            print(f"Author name        :: {self.author}")
            print(f"Year               :: {self.year}")
            print(f"Title of chapter   :: {self.title_chapter}")
            print(f"Editor name        :: {self.editor}")
            print(f"Title of Book      :: {self.title_book}")
            print(f"Page range         :: {self.prange}")
            print(f"Publisher          :: {self.publisher}")
            print(f"In text citation 1 :: {self.intext}")
            print(f"In text citation 2 :: {self.in_text}")
            print(f"Reference          :: {self.reference}")        
            print("======================================================================")
           
        def Authors(self, Authors):
            names = list(Authors)
            str_name = []
            for author in names:
                if len(author.split(' ')) == 2:
                     first, last = author.split(' ')
                     name = first.title() + ', ' + last.title()[0] + '.'
                     str_name.append(name)
                elif len(author.split(' ')) == 3:
                     first, middle, last = author.split(' ')
                     name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                     str_name.append(name)
                else:
                     str_name.append(author + '. ')
            
            names = ''
            if len(str_name) > 1:
                for name in str_name:
                    if str_name[-1] != name:
                        names += name + ' '
                    else:
                        names += '& ' + name
            else:
                names = str_name[0]
            
            self.author = names
        
        def Editors(self, Authors):
            names = list(Authors)
            str_name = []
            for author in names:
                if len(author.split(' ')) == 2:
                     first, last = author.split(' ')
                     name = first.title() + ', ' + last.title()[0] + '.'
                     str_name.append(name)
                elif len(author.split(' ')) == 3:
                     first, middle, last = author.split(' ')
                     name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                     str_name.append(name)
                else:
                     str_name.append(author + '. ')
            
            names = ''
            if len(str_name) > 1:
                for name in str_name:
                    if str_name[-1] != name:
                        names += name + ' '
                    else:
                        names += '& ' + name
            else:
                names = str_name[0]
            
            self.editor = names    
           
        def Title_chapter(self, title):
            self.title_chapter = title
        
        def Title_book(self, title):
            self.title_book = title
        
        def Year(self, year):
            self.year = year
            
        def Publisher(self, publisher):
            self.publisher = publisher
 
        def ref(self):
            if self.author == '':
                reference = f"{self.title_chapter} ({self.year}). In {self.editor} (Eds.), <i>{self.title_book}</i> (pp. {self.prange}). {self.publisher}"      
            else:
                reference = f"{self.author} ({self.year}). {self.title_chapter}. In {self.editor} (Eds.), <i>{self.title_book}</i> (pp. {self.prange}). {self.publisher}"      
            name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
            name = ' '.join(name)
            if len(name.split(' ')) > 4:
                intext = f"({name.split(' ')[0]} et al. ({self.year})"
                in_text = f"{name.split(' ')[0]} et al. ({self.year})"
            else:
                intext = f"({name}, {self.year})"
                in_text = f"{name}, {self.year})"
            self.intext = intext
            self.in_text = in_text
            self.reference = reference
            self.info()    
            
        def Page_range(self, prange):
            self.prange = prange
        
        def Title_ref(self, title):
            self.title_ref = title
    
    class edited:
        def __init__(self, editor='', year='', title_of_book='', publisher='', url=''):
            self.editor = editor
            self.title_book = title_of_book
            self.year = year
            self.publisher = publisher
            self.source = url
            self.intext = ''
            self.in_text = ''
            self.reference = ''
            self.info()
        
        def info(self):
            print(" _____    _ _ _           _   _                 _")
            print("| ____|__| (_) |_ ___  __| | | |__   ___   ___ | | __")
            print("|  _| / _` | | __/ _ \/ _` | | '_ \ / _ \ / _ \| |/ /")
            print("| |__| (_| | | ||  __/ (_| | | |_) | (_) | (_) |   <")
            print("|_____\__,_|_|\__\___|\__,_| |_.__/ \___/ \___/|_|\_\\")
            print("======================================================================")
            print("Current course material has information")
            print("======================================================================")
            print(f"Editor name        :: {self.editor}")
            print(f"Year               :: {self.year}")
            print(f"Title of book      :: {self.title_book}")
            print(f"Source             :: {self.source}")
            print(f"Publisher          :: {self.publisher}")
            print(f"In text citation 1 :: {self.intext}")
            print(f"In text citation 2 :: {self.in_text}")
            print(f"Reference          :: {self.reference}")        
            print("======================================================================")
    
        def Year(self, year):
            self.year = str(year)
    
        def Editors(self, Authors):
                names = list(Authors)
                str_name = []
                for author in names:
                    if len(author.split(' ')) == 2:
                         first, last = author.split(' ')
                         name = first.title() + ', ' + last.title()[0] + '.'
                         str_name.append(name)
                    elif len(author.split(' ')) == 3:
                         first, middle, last = author.split(' ')
                         name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                         str_name.append(name)
                    else:
                         str_name.append(author + '. ')
                
                names = ''
                if len(str_name) > 1:
                    for name in str_name:
                        if str_name[-1] != name:
                            names += name + ' '
                        else:
                            names += '& ' + name
                else:
                    names = str_name[0]
                
                self.editor = names    
                
        def Title(self, title):
            self.title_book = title
        
        def Publisher(self, publisher):
            self.publisher = publisher
        
        def ref(self):
            reference = f"{self.editor} ({self.year}). <i>{self.title_book}</i>. {self.publisher}. {self.source}"      
            name = [name.strip(',').strip('.') for name in self.editor.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
            name = ' '.join(name)
            if len(name.split(' ')) > 3:
                intext = f"({name.split(' ')[0]} et al. ({self.year})"
                in_text = f"{name.split(' ')[0]} et al. ({self.year})"
            else:
                intext = f"({name}, {self.year})"
                in_text = f"{name}, {self.year})"
            self.intext = intext
            self.in_text = in_text
            self.reference = reference
            self.info()    
         
        def Source(self, url):
            self.source = url
            
    class electronic:
        def __init__(self, author='', year='', title_of_book='', publisher='', url=''):
            self.author = author
            self.title_book = title_of_book
            self.year = year
            self.publisher = publisher
            self.source = url
            self.intext = ''
            self.in_text = ''
            self.reference = ''
            self.info()
        
        def info(self):
            print(" _____ _           _                   _")
            print("| ____| | ___  ___| |_ _ __ ___  _ __ (_) ___")
            print("|  _| | |/ _ \/ __| __| '__/ _ \| '_ \| |/ __|")
            print("| |___| |  __/ (__| |_| | | (_) | | | | | (__")
            print("|_____|_|\___|\___|\__|_|  \___/|_| |_|_|\___|")
            print("======================================================================")
            print("Current course material has information")
            print("======================================================================")
            print(f"Author name        :: {self.author}")
            print(f"Year               :: {self.year}")
            print(f"Title of book      :: {self.title_book}")
            print(f"Source             :: {self.source}")
            print(f"Publisher          :: {self.publisher}")
            print(f"In text citation 1 :: {self.intext}")
            print(f"In text citation 2 :: {self.in_text}")
            print(f"Reference          :: {self.reference}")        
            print("======================================================================")
    
        def Year(self, year):
            self.year = str(year)
    
        def Author(self, Authors):
                names = list(Authors)
                str_name = []
                for author in names:
                    if len(author.split(' ')) == 2:
                         first, last = author.split(' ')
                         name = first.title() + ', ' + last.title()[0] + '.'
                         str_name.append(name)
                    elif len(author.split(' ')) == 3:
                         first, middle, last = author.split(' ')
                         name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                         str_name.append(name)
                    else:
                         str_name.append(author + '. ')
                
                names = ''
                if len(str_name) > 1:
                    for name in str_name:
                        if str_name[-1] != name:
                            names += name + ' '
                        else:
                            names += '& ' + name
                else:
                    names = str_name[0]
                
                self.author = names    
                
        def Title(self, title):
            self.title_book = title
        
        def Publisher(self, publisher):
            self.publisher = publisher
        
        def ref(self):
            reference = f"{self.author} ({self.year}). <i>{self.title_book}</i>. {self.publisher}. {self.source}"      
            name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
            name = ' '.join(name)
            if len(name.split(' ')) > 4:
                intext = f"({name.split(' ')[0]} et al. ({self.year})"
                in_text = f"{name.split(' ')[0]} et al. ({self.year})"
            else:
                intext = f"({name}, {self.year})"
                in_text = f"{name}, {self.year})"
            self.intext = intext
            self.in_text = in_text
            self.reference = reference
            self.info() 
            
        def Source(self, url):
            self.source = url
    
    class secondary_source:
        def __init__(self, author='',year='',title_book='',publication_place='',publisher=''):
            self.author = author
            self.title = title_book
            self.place = publication_place
            self.publisher = publisher
            self.year = year
            self.intext = ''
            self.in_text = ''
            self.reference = ''
            self.info()
        
        def info(self):
            print(" ____                           _")
            print("/ ___|  ___  ___ ___  _ __   __| | __ _ _ __ _   _")
            print("\___ \ / _ \/ __/ _ \| '_ \ / _` |/ _` | '__| | | |")
            print(" ___) |  __/ (_| (_) | | | | (_| | (_| | |  | |_| |")
            print("|____/ \___|\___\___/|_| |_|\__,_|\__,_|_|   \__, |")
            print("                                             |___/")
            print("======================================================================")
            print("Current course material has information")
            print("======================================================================")
            print(f"Author name        :: {self.author}")
            print(f"Year               :: {self.year}")
            print(f"Title of book      :: {self.title}")
            print(f"Publication place  :: {self.place}")
            print(f"Publisher          :: {self.publisher}")
            print(f"In text citation 1 :: {self.intext}")
            print(f"In text citation 2 :: {self.in_text}")
            print(f"Reference          :: {self.reference}")        
            print("======================================================================")
        
        def Title(self, title):
            self.title = title
        
        def Publisher(self, publisher):
            self.publisher = publisher
            
        def Place(self, place):
            self.place = place
            
        def Author(self, Authors):
                names = list(Authors)
                str_name = []
                for author in names:
                    if len(author.split(' ')) == 2:
                         first, last = author.split(' ')
                         name = first.title() + ', ' + last.title()[0] + '.'
                         str_name.append(name)
                    elif len(author.split(' ')) == 3:
                         first, middle, last = author.split(' ')
                         name = first.title() + ', ' + middle.title()[0] + '. ' + last.title()[0] + '.'
                         str_name.append(name)
                    else:
                         str_name.append(author + '. ')
                
                names = ''
                if len(str_name) > 1:
                    for name in str_name:
                        if str_name[-1] != name:
                            names += name + ' '
                        else:
                            names += '& ' + name
                else:
                    names = str_name[0]
                
                self.author = names   
         
        def ref(self):
            reference = f"{self.author} ({self.year}). <i>{self.title}</i>. {self.place}. {self.publisher}."      
            name = [name.strip(',').strip('.') for name in self.author.split(' ') if len(name.strip(',').strip('.')) > 1 or name.strip(',').strip('.') == '&']
            name = ' '.join(name)
            if len(name.split(' ')) > 4:
                intext = f"({name.split(' ')[0]} et al. ({self.year})"
                in_text = f"{name.split(' ')[0]} et al. ({self.year})"
            else:
                intext = f"(as cited in {name}, {self.year})"
                in_text = f"as cited in {name}, {self.year})"
            self.intext = intext
            self.in_text = in_text
            self.reference = reference
            self.info() 
            
ref_15 = books().secondary_source(year = '1983')
ref_15.Publisher('NY: McGraw-Hill')
ref_15.Title('Introduction to psychology: A reader')
ref_15.Place('New York')
ref_15.Author(['Smith P', 'Jones M', 'Black J'])
ref_15.ref()