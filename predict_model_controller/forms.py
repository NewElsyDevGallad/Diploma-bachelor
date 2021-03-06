from django import forms
from django.forms import TextInput


class ModelPredictForm(forms.Form):
    educ_form_choices = [("Заочная", "Заочная"),
                         ("Очная", "Очная"),
                         ("Очно-заочная", "Очно-заочная")]
    qualification_choices = [("Бакалавр", "Бакалавр"),
                             ("Магистр", "Магистр"),
                             ("Специалист", "Специалист")]
    course_choices = [("1", "1"),
                      ("2", "2"),
                      ("3", "3"),
                      ("4", "4"),
                      ("5", "5")]
    profile_list = ['Автоматизация теплоэнергетических процессов',
                    'Автоматизация технологических процессов и производств (в нефтегазовой отрасли)',
                    'Автоматизация технологических процессов и производств в машиностроении',
                    'Автоматизация технологических процессов и производств в нефтяной и газовой промышленности',
                    'Автоматизация технологических процессов и производств в теплоэнергетике и теплотехнике',
                    'Аддитивные технологии', 'Анализ и контроль в биотехнологических и фармацевтических производствах',
                    'Безопасность и нераспространение ядерных материалов', 'Биомедицинская инженерия',
                    'Биотехнические и медицинские аппараты и системы', 'Биотехнология',
                    'Бурение нефтяных и газовых скважин', 'Бухгалтерский учет, анализ и аудит',
                    'Высоковольтные электроэнергетика и электротехника',
                    'Вычислительные машины, комплексы, системы и сети', 'Геоинформационные системы',
                    'Геологическая съемка, поиски и разведка месторождений твердых полезных ископаемых',
                    'Геология месторождений стратегических металлов', 'Геология нефти и газа',
                    'Геофизические методы исследования скважин', 'Геоэкология', 'Защита в чрезвычайных ситуациях',
                    'Землеустройство', 'Изотопные технологии и материалы', 'Инженерное предпринимательство',
                    'Инженерные изыскания в области природообустройства',
                    'Инжиниринг нефтегазоперерабатывающих и нефтехимических производств',
                    'Интеллектуальные робототехнические и мехатронные системы',
                    'Интеллектуальные системы автоматизации и управления',
                    'Информационно-измерительная техника и технологии',
                    'Информационно-измерительная техника и технологии неразрушающего контроля',
                    'Информационно-коммуникационные технологии',
                    'Информационно-телекоммуникационные системы и технологии (Networks and Communications)',
                    'Информационные системы и технологии в бизнесе',
                    'Информационные системы и технологии в неразрушающем контроле и безопасности',
                    'Информационные технологии в электроэнергетике',
                    'Информационные технологии управления производственными процессами',
                    'Киберфизическая автоматизация высокотехнологичных процессов и производств',
                    'Компьютеризация измерений и контроля', 'Компьютерное моделирование',
                    'Компьютерный анализ и интерпретация данных', 'Конструирование технологического оборудования',
                    'Конструкторско-технологическое обеспечение автоматизированных машиностроительных производств',
                    'Котлы, камеры сгорания и парогенераторы АЭС', 'Математические методы в экономике',
                    'Математическое моделирование и компьютерные вычисления',
                    'Материаловедение и технологии материалов',
                    'Материаловедение и технология материалов в машиностроении',
                    'Машины и аппараты химических производств', 'Машины и оборудование нефтяных и газовых промыслов',
                    'Машины и технологии сварочного производства',
                    'Машины и технология высокоэффективных процессов обработки материалов',
                    'Медицинские информационные системы и телемедицина', 'Надежность газонефтепроводов и хранилищ',
                    'Наноструктурные материалы', 'Нет', 'Нефтегазопромысловая геология',
                    'Обеспечение эффективности технологических процессов жизненного цикла изделий',
                    'Оборудование и технология сварочного производства', 'Оптико-электронные приборы и системы',
                    'Основные процессы химических производств и химическая кибернетика',
                    'Перспективные химические и биомедицинские технологии',
                    'Плазменно-пучковые и электроразрядные технологии',
                    'Поиски и разведка подземных вод и инженерно-геологические изыскания',
                    'Предпринимательство в инновационной деятельности', 'Приборостроение',
                    'Приборы и методы контроля качества и диагностики', 'Прикладная электронная инженерия',
                    'Прикладной системный инжиниринг',
                    'Применение математических методов к решению инженерных и экономических задач',
                    'Проектирование и эксплуатация атомных станций', 'Производственный менеджмент',
                    'Производство и транспортировка электрической энергии',
                    'Производство изделий из наноструктурных материалов', 'Промышленная теплоэнергетика',
                    'Промышленная томография сложных систем', 'Промышленная электроника', 'Промышленный дизайн',
                    'Пучковые и плазменные технологии', 'Радиационная безопасность человека и окружающей среды',
                    'Разработка и эксплуатация нефтяных и газовых месторождений', 'Разработка интернет-приложений',
                    'Разработка программно-информационных систем', 'Разработка трудноизвлекаемых запасов углеводородов',
                    'Релейная защита и автоматизация электроэнергетических систем',
                    'Релейная защита и автоматика энергосистем', 'Системная инженерия программного обеспечения',
                    'Системы автоматизации физических установок и их элементы',
                    'Системы управления технологическими процессами и физическими установками',
                    'Строительство глубоких нефтяных и газовых скважин в сложных горно-геологических условиях',
                    'Тепловые и атомные электрические станции', 'Тепловые электрические станции',
                    'Техника и физика высоких напряжений', 'Технологии больших данных',
                    'Технологии водородной энергетики', 'Технологии наукоемких производств в машиностроении',
                    'Технологии проектирования, производства и диагностирования энергетического оборудования',
                    'Технологии промышленной теплотехники', 'Технологии радиационной безопасности',
                    'Технологическое брокерство', 'Технология и оборудование химических и нефтехимических производств',
                    'Технология и техника разведки месторождений полезных ископаемых',
                    'Технология нефтегазохимии и полимерных материалов',
                    'Технология тугоплавких неметаллических и силикатных материалов',
                    'Технология, оборудование и автоматизация машиностроительных производств',
                    'Управление в производственных системах', 'Управление земельными ресурсами',
                    'Управление качеством в производственно-технологических системах',
                    'Управление комплексной техносферной безопасностью',
                    'Управление режимами электроэнергетических систем', 'Управление роботами и мехатронными системами',
                    'Управление ядерной энергетической установкой', 'Физика атомного ядра и частиц',
                    'Физика кинетических явлений', 'Физика конденсированного состояния вещества',
                    'Фотонные технологии и светотехническая инженерия',
                    'Химическая технология высокомолекулярных соединений',
                    'Химическая технология керамики и композиционных материалов',
                    'Химическая технология материалов ЯТЦ', 'Химическая технология материалов ядерно-топливного цикла',
                    'Химическая технология органических веществ',
                    'Химическая технология подготовки и переработки нефти и газа',
                    'Химическая технология природных энергоносителей и углеродных материалов',
                    'Химическая технология синтетических биологически активных веществ, химико-фармацевтических препаратов и косметических средств',
                    'Химическая технология топлива и газа', 'Химические технологии в биологии и медицине',
                    'Химический инжиниринг', 'Химия и технология биологически активных веществ', 'Цифровой маркетинг',
                    'Чистая вода', 'Экологические проблемы окружающей среды', 'Экономика и управление на предприятии',
                    'Экономика и управление на предприятии нефтегазовой отрасли', 'Экономика предприятий и организаций',
                    'Эксплуатация и обслуживание оборудования газокомпрессорных станций',
                    'Эксплуатация и обслуживание объектов добычи нефти',
                    'Эксплуатация и обслуживание объектов транспорта и хранения нефти, газа и продуктов переработки',
                    'Эксплуатация и обслуживание объектов транспорта и хранения углеводородов', 'Электрические станции',
                    'Электрические станции и подстанции, высоковольтная техника',
                    'Электроизоляционная, кабельная и конденсаторная техника',
                    'Электроизоляционные системы и кабельная техника', 'Электромеханика',
                    'Электромеханические и электротехнические системы автономных объектов',
                    'Электрооборудование и электрохозяйство предприятий, организаций и учреждений',
                    'Электрооборудование летательных аппаратов',
                    'Электропривод и автоматизация электротехнических комплексов и систем',
                    'Электропривод и автоматика', 'Электроснабжение',
                    'Электроснабжение и автоматизация объектов нефтегазовой промышленности',
                    'Электроснабжение промышленных предприятий и городов', 'Электроэнергетические системы и сети',
                    'Энергосберегающие режимы электрических источников питания и электротехнических установок',
                    'Ядерная медицина (медицинская физика)', 'Ядерные реакторы и энергетические установки']
    profile_choices = zip(profile_list, profile_list)
    dep_list = ['Исследовательская школа химических и биомедицинских технологий',
                'Научно-образовательный центр Б.П. Вейнберга', 'Научно-образовательный центр И.Н.Бутакова',
                'Научно-образовательный центр Н.М.Кижнера', 'Отделение автоматизации и робототехники',
                'Отделение геологии', 'Отделение информационных технологий', 'Отделение контроля и диагностики',
                'Отделение материаловедения', 'Отделение нефтегазового дела', 'Отделение социально-гуманитарных наук',
                'Отделение химической инженерии', 'Отделение экспериментальной физики',
                'Отделение электронной инженерии', 'Отделение электроэнергетики и электротехники',
                'Отделение ядерно-топливного цикла', 'Школа инженерного предпринимательства']
    dep_choices = zip(dep_list, dep_list)
    subdep_list = ['Инженерная школа информационных технологий и робототехники',
                   'Инженерная школа неразрушающего контроля и безопасности',
                   'Инженерная школа новых производственных технологий', 'Инженерная школа природных ресурсов',
                   'Инженерная школа энергетики', 'Инженерная школа ядерных технологий',
                   'Исследовательская школа химических и биомедицинских технологий',
                   'Школа инженерного предпринимательства']
    subdep_choices = zip(subdep_list, subdep_list)
    fin_list = ['на договорной основе', 'на основе бюджетного финансирования', 'по целевому приёму']
    fin_choices = zip(fin_list, fin_list)
    citizenship_list = ['Алжирская Народная Демократическая Республика', 'Арабская Республика Египет',
                        'Без гражданства', 'Государство Израиль', 'Демократическая Республика Конго',
                        'Йеменская Республика', 'Киргизская Республика', 'Китайская Народная Республика',
                        'Королевство Марокко', 'Монголия', 'Народная Республика Бангладеш',
                        'Переходное Исламское Государство Афганистан', 'Республика Айзербайджан', 'Республика Беларусь',
                        'Республика Боливия', 'Республика Гана', 'Республика Гватемала', 'Республика Замбия',
                        'Республика Зимбабве', 'Республика Индия', 'Республика Индонезия', 'Республика Ирак',
                        'Республика Казахстан', 'Республика Казахстан, Российская Федерация', 'Республика Колумбия',
                        'Республика Конго', 'Республика Корея', 'Республика Мозамбик', 'Республика Молдова',
                        'Республика Намибия', 'Республика Судан', 'Республика Таджикистан',
                        'Республика Таджикистан, Российская Федерация', 'Республика Узбекистан', 'Российская Федерация',
                        'Социалистическая Республика Вьетнам', 'Туркменистан', 'Украина',
                        'Федеративная Республика Бразилия', 'Федеративная Республика Нигерия', 'Эстонская Республика',
                        'Южно-Африканская Республика']
    citizenship_choices = zip(citizenship_list, citizenship_list)
    gender_choices = [("Женский", "Женский"),
                      ("Мужской", "Мужской")]
    vacation_choices = [("Да", "Да"),
                        ("Нет", "Нет")]

    educ_form = forms.ChoiceField(choices=educ_form_choices,
                                  widget=forms.Select(attrs={'class': 'form-control select2'}))
    qualification = forms.ChoiceField(choices=qualification_choices,
                                      widget=forms.Select(attrs={'class': 'form-control select2'}))
    course = forms.ChoiceField(choices=course_choices, widget=forms.Select(attrs={'class': 'form-control select2'}))
    profile = forms.ChoiceField(choices=profile_choices, widget=forms.Select(attrs={'class': 'form-control select2'}))
    dep = forms.ChoiceField(choices=dep_choices, widget=forms.Select(attrs={'class': 'form-control select2'}))
    subdep = forms.ChoiceField(choices=subdep_choices, widget=forms.Select(attrs={'class': 'form-control select2'}))
    fin = forms.ChoiceField(choices=fin_choices, widget=forms.Select(attrs={'class': 'form-control select2'}))
    citizenship = forms.ChoiceField(choices=citizenship_choices,
                                    widget=forms.Select(attrs={'class': 'form-control select2'}))
    gender = forms.ChoiceField(choices=gender_choices, widget=forms.Select(attrs={'class': 'form-control select2'}))
    vacation = forms.ChoiceField(choices=vacation_choices, widget=forms.Select(attrs={'class': 'form-control select2'}))

    educ_hours = forms.CharField(
        widget=TextInput(attrs={'type': 'number', 'class': 'form-control', 'placeholder': '408'}))
