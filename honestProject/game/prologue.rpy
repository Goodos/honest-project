label prologue:
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # play music "audio/ye.mp3" fadeout 1.0 fadein 1.0

    scene bg dream with fade:
        blur 3
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    "Сквозь пелену сна к тебе тянется чья-то рука. Кончики пальцев
    нежно касаются твоей щеки. Пальцы обжигают твою щёку могильным
    холодом, словно весенняя капель пробирающаяся сквозь последние
    сугробы. Просто прикосновение. Не больше, не меньше. Ты не
    можешь вспомнить чьи это руки. Как не можешь вспомнить когда
    оно произошло. Но почему-то ты уверен полностью, что это
    прощальное прикосновение."

    scene bg roomCastle
    with fade

    show lieut idle #at right
    with dissolve

    lieut "Учитель!" 
    with vpunch

    #hide lieut
    #with dissolve

    "Громкий стук в дверь возвращает тебя в реальный мир. Видимо,
    случилось что-то срочное, раз твой помощник пришёл лично будить
    тебя. Хорошо потянувшись, ты запрыгиваешь в тапочки и,
    почёсывая бок направляешься к двери."

    #show lieut idle #at left with dissolve

    lieut "Учитель, доброе утро!"

    me "Доброе" #with vpunch
    
    lieut "Вас срочно вызывают на аудиенцию к Монарху."

    "В столь ранний час?"

    me "Хорошо, передай что я буду в Тронном зале через двадцать минут."

    hide lieut
    with dissolve

    "После небольшого реверанса твой помощник быстрым шагом
    удаляется. Ты же принимаешься за утренние ритуалы. Молитва,
    умывание и зарядка. Завтрак придёться заменить поздним бранчем,
    но это не страшно. На выходе из Соборных спален столпились
    мелкие церковные служащие. На твое \"доброе утро\" они лишь
    учтиво кивают головами. Столько лет прошло с твоего назначения
    на должность главного дознавателя Святой Инквизиции, а твои
    \"коллеги\" всё никак не могут смирится с тем фактом, что ты
    \"полукровка\"."

    "\"Неслыханное святотатство!\" - только и заявил Верховный дьякон
    перед тем, как отречься от своего поста и постричься в монахи.
    Он принял обет молчания и уехал жить в отшельничестве на остров
    Марии мученицы, пока ты осваивал свой новый кабинет в Столичном
    Соборе."

    "Монарх никогда не звал тебя \"полукровкой\". Начатая в детстве
    дружба с годами лишь крепла. И для монарха она стала чем-то
    незыблимым, после того, как его отец был подло отравлен. В этот
    день, ваш близкий друг окончательно превратился в мужчину."

    "Пересекая Соборную площадь и дальше - всю дорогу к Дворцу - ты
    продолжал думать о ладони, что коснулась тебя во сне. Сны -
    редкость для тебя. Зачастую даже пытка. Неясные образы из
    прошлого преследуют тебя всё навязчивей и навязчивей в
    последние недели. Лучший следователь, поймавший всю секту
    \"Праведная Луна\", что активно терроризировала государства из
    подполья. И никак не можешь разгадать загадку собственной души.
    Мда уж…"

    scene bg hallwayCastle
    with fade

    "В коридоре твой острый слух выхватывает обрывки разговора двух
    стражников, охраняющих Тронный зал"

    show guardian1 idle at left
    with dissolve

    show guardian2 idle at right
    with dissolve

    guardian1 "Подумать только, сначала Государь призывает
    на аудиенцию Архимагистра Ордена. Теперь
    верховного дознавателя…Что-то плохое
    намечается."

    guardian2 "Нечего тебе рассуждать об этом. Не наше с тобой дело. Мы тут на дозоре, не забывай. А то сам знаешь, как оно бывает. Раз и…
    Поминай как звали."

    "При виде тебя стражники вздрогнули и замерли в стойке \"смирно\""

    menu:

        "Доброго утра, солдаты":
            jump toHall

        "Правильно, послушай своего товарища. Я на плаху и за меньшее отправлял.":
            jump toHall

        "Промолчать":
            jump toHall

    label toHall:
        "Один из стражников открывает перед вами двери, пока другой
        громко проглатывает комок, застрявший в горле. Ты пару раз
        хлопаешь его по плечу"

        me "Не волнуйся, солдат, пока ты с честью
        выполняешь долг перед отчизной, такие как я
        тебе ничего сделать не смогут. Разве что
        похвалить лишний раз."

        guardian2 "Благодарю, сэр!"

    scene bg hallCastle
    with fade

    "Сложно сказать, когда тронный зал претерпел столь резкие
    изменения в обстановке. Но от кричащих и ярких полотен, которые
    так любил отец, Монарх отказался в сторону тёмных и синих
    тонов. В это время дня никого кроме Государя и его служанок в
    зале не было. Молодые девушки из потомственных родов-слуг
    окружают заботой Монарха в повседневных делах. И не только в
    них. Одна из них прямо сейчас подливает ещё вина в бокал
    Монарха. Твой старый друг стоит спиной к тебе и рассматривает
    что-то за окном на улице. Ты подходишь поближе и падаешь на
    одно колено."

    me "Ваше величество"

    show monarch idle
    with dissolve

    "Монарх оборачивается и на его лице сияет улыбка. Розовые щёки и
    покрасневший нос свидетельствуют о том, что он давно пил. А
    синяки под глазами есть примета неспокойной ночи."

    monarch "А, мой старый друг! Как же я рад тебя видеть. Вина?"

    "Не дожидаясь твоего ответа, Монарх щёлкает пальцами и в твоей руке тут же оказывает бокал, полный изящного и дорогого вина."

    monarch "И так, мы позвали за тобой для очень важного дела. Речь идёт о государственной измене. Орден готовит, не побоюсь этого слова, переворот.?"

    "Орден? Измена? Переворот? Как такое может быть? Ты знаком с
    летописями Крестовых походов и в чём никогда не мог усомниться,
    так это в лояльности Ордена к Церкви и Монарху. В конце концов,
    именно Орден всегда был в авангарде армии. Именно Орден нёс
    самые большие потери в походах на эльфов. Вот уж действительно
    экстраординарное утро. Может твой друг перебрал с вином? При
    дворе ходят слухи про его злоупотребление альгулем…К сожалению,
    ты лишь недавно вернулся с поимки \"Правдивой Луны\". Операция
    затянулась и ты пробыл в западных землях больше, чем
    требовалось. Кажется, именно тогда в твои сновиденья стали
    пробиваться обрывки воспоминаний. Если бы не это прикосновение…"

    #возможно сделать смену лица монарха - с обычной ухмылки на озабоченное
    show monarch concern
    with dissolve

    monarch "Инквизитор, с вами всё впорядке?"
    
    "Этим вопросом он возвращает тебя к реальности. Уголки твоего
    рта легко и непринуждённо приподнимаются в улыбке. Сейчас и
    вправду не стоит мечтать, нужно сосредоточиться над делами
    насущными."

    me "Не волнуйтесь, Ваше Величество, небольшое
    расстройство желудка."

    #смена лица - с озабоченной на обычную
    show monarch idle
    with dissolve

    "Краска озабоченности быстро сползает с лица Монарха и уступает
    место флегматичному тону. Которое ты так привык видеть. Хоть вы
    и росли вместе, всё же между вами пролегла целая пропасть из
    статусов, привелегий и ответственности. Монарх одним глотком
    осушает свой бокал вина и тут же зовёт служанку наполнить его
    по новой. Не забывая про этикет, ты пригубил немного вина. Пить
    в такой ранний час всё же привелегия Монарха, а не скромного
    слуги Инквизиции."

    monarch "Ты должен понимать, насколько важно для нас
    достичь абсолютного успеха в этом задании."

    "Обычно Правителю нет никакого дела до твоей службы в
    Инквизиции. Ваши беседы несут скорее дружеский характер.
    Возможно, с возрастом Монарху становится всё тяжелее отличать
    друзей от врагов. Дворовые интригы проступают на его лице
    маленькими морщинками в уголках глаз. И видеть твоё всё ещё
    юное лицо помогает ему вспомнить свою ушедшую беззаботную
    юность."

    monarch "Власть ордена на восточной границе
    приобрела слишком большой масштаб. Мои
    шпионы давно следят за их деятельностью, на
    случай, если они начнут представлять
    опасность для моей власти. Всё же организация такого масштаба… 
    С их опытом и вооружением они могут легко снести всю мою
    Королевскую рать."

    monarch "По донесению моих самых доверенных
    разведчиков, в ходе третьего крестового
    похода Архимагистр Ордена вступила в сговор
    с Королевой эльфов. По прибытию на Родину,
    Архимагистр стала подготавливать почву для
    эльфиского вторжения на наши земли…"

    #смена лица - злое лицо
    show monarch angry
    with dissolve

    "Ладонь правой руки монарха постепенно сжимается в кулак."

    monarch "Мою землю…"

    "Монарх делает жадный глоток, перед тем как продолжить"

    monarch "К сожалению, я не могу официально выступить
    против Ордена. Пока у нас не будет везких
    доказательств в их измене. Вверенные им под
    управление земли обеспечивают две трети
    нашего государства зерном. Военные
    советники утверждают, что в случае
    открытого конфликта нас ждёт бунт среди
    крестьян. Подкреплённый войсками Ордена и
    эльфийскими партизанами. Мы не можем пойти
    на это. Мы должны быть умнее, хитрее.
    Поэтому ты поедешь туда, как верный слуга
    Церкви. Официально твой титул - Старший
    Дознаватель. Именно чины такого ранга
    допускаются за двери Ордена. Знать им о
    твоём реальном положении в обществе - ни к
    чему. Все инструкции и сопутствующие к делу
    материалы уже пакуют в твои сумки. Экипаж
    будет ждать тебя после обеда."

    menu:

        "Я слышал, что Архимагистр ордена вчера прибыла в столицу на королевскую аудиенцию. Где она сейчас?":
            jump monarchDialogueAboutMission

        "Сколько времени отводится на выполнение задачи?":
            jump monarchDialogueAboutMission

        "Разрешите откланяться, Ваше Величество.":
            jump monarchDialogueAboutMission

    label monarchDialogueAboutMission:

        monarch "Мы пригласили её для обсуждения ренноваций,
        в коих столь сильно нуждается наша Церковь.
        Неудача последнего крестового похода стоила
        слишком много для нашей казны. Военные и
        экономические отчёты совместно трубят о
        неэффективности распределения наших
        активов. К следующему посевному урожаю мы
        должны утвердить новые налоги, пересмотреть
        старые. Работы много, поэтому в нашем
        письме мы заявляли о посещении столицы на
        долгий срок. Архимагистр с радостью приняла
        приглашение. Ведь зимой без крестовых
        походов Ордену разве что беднякам хлеб
        раздавать остаётся. Конечно, по приезду мы
        схватили её и отправили в темницу. Сейчас
        мои мастера пыток раскалёными клешнями
        тянут из неё признание, но она стоически
        терпит боль. Не произносит ни звука. Да…
        Вот это выдержка. Впрочем, не следует
        ожидать чего-то меньшего от самого
        Архимагистра."

        me "Могу ли я побеседовать с Архимагистром перед отъездом?"

        monarch "Конечно, мой дорогой друг! Может быть тебе
        удастся вытащить из этой грязной еретички
        признание. Только сильно у неё не
        задерживайся, в конце-концов впереди тебя
        ждёт дальняя дорога."

        "Ты опускаешься на одно колено, в знак прощания. Но Монарх небрежным движением руки велит тебе подняться."

        #смена лица - доброе лицо
        show monarch idle
        with dissolve

        monarch "Оставь эти формальности!"

        "Монарх подходит к вам ближе и заключает в крепкие тёплые объятия."

        monarch "Мы будем с нетерпением ждать от тебя новостей."

        "Ты не хочешь давать ложную надежду Монарху, ведь пока что дело
        вырисовывается слишком странным. Поэтому на прощание ты молча
        киваешь ему и выходишь из тронного зала."

    label dungeonInCastle:
        scene bg dungeonCastle
        with fade

        "Темница, скрытая в катакомбах Старого Дворца. Клетка, в которой заточена Архимагистр."

        show archMaster exhausted
        with dissolve

        "Сейчас у палачей обеденный перерыв. Поэтому Архимагистра ты
        застаёшь одну, в полуобморочном состоянии. Она прикована
        стальными цепями по рукам и ногам. Множественные ссадины и
        подтёки с ожогами на теле свидетельствуют о продолжительных
        побоях. Но ты подмечаешь, что кости с ногтями целы. Значит,
        Монарх пока ещё не отдал приказ переходить к более радикальным
        мерам. Голова Архимагистра бессильно опустилась на её грудь.
        Она тяжело дышит, жадно глотая спёртый воздух подземелья своими
        потрескавшимися губами. Лохмотья, в которые превратилась её
        одежда, едва скрывают самые постыдные участки тела. Ты хорошо
        знаешь, что когда начнутся настоящие пытки, с неё сорвут даже
        это. Услышав ваши шаги Архимагистр приподнимает голову, она
        щурится, пытаясь разобрать кто же перед ней стоит"

        archMaster "Не припомню вас в рядах палачей. Пришли сменить своих товарищей?"

        menu:

            "Мои методы более гуманны. Я пришёл просто поговорить.":
                jump dungeonCastleArchMasterDialogue1

            "Ничто бы мне не доставило большего наслаждения, как пытки скверной еретички. Но увы, я здесь не за этим.":
                jump dungeonCastleArchMasterDialogue1

            "Мне больно видеть великого Архимагистра Ордена в таком виде. Обвинённого в ереси, закованного в цепи, униженного…":
                jump dungeonCastleArchMasterDialogue1
        
        label dungeonCastleArchMasterDialogue1:

            archMaster "Боюсь с разговором вы уже опоздали. Так кто вы такой? Очередной слуга Его Величества?"

            me "Я главный дознаватель Святой Инквизиции."

            archMaster "Вон оно как… Уверена Монарх успел посвятить
            вас во все детали происходящего. Уверена
            так же что именно вас он избрал быть
            палачом моего Ордена."

            menu:

                "Именно так. Мне выпала честь нести справедливость от имени Монарха и Святой Церкви.":
                    jump dungeonCastleArchMasterDialogue2

                "Можешь быть уверена ещё и в том, что каждый замешанный в твоей ереси понесёт справедливое возмездие. А потом… Я приду за тобой.":
                    jump dungeonCastleArchMasterDialogue2

                "За свою службу в рядах Инквизиции я
                судил многих: фермеров, обратившихся к
                древним ритуалам; купцов, торговавших с
                эльфами; богатеев, коллекционирующих
                запретные артефакты; даже дворян, упавших в
                сладострастные руки порока. Но воинов
                Церкви, такое будет впервые.":
                    jump dungeonCastleArchMasterDialogue2

            label dungeonCastleArchMasterDialogue2:

                show archMaster idle
                with dissolve

                "На мгновение тебе кажется, что к Архимагистру вернулась острота
                понимания происходящего. Её широкая грудь вздымается, пока она
                делает глубокий вдох. После третьего вдоха глаза Архимагистра
                вновь сияют яркой синевой. Её тренированное тело дрожит, от
                напряжения."

                archMaster "Послушайте меня, Дознаватель. То, что вы
                обнаружите в Ордене не то, чем кажется. Я
                прошу вас не судить моих сестёр. Если я
                грешна, то сама и понесу за это наказание.
                Но я никогда не признаюсь в государственной
                измене. Монарх не говорит вам всей правды.
                На самом деле…"

                "На последнем слове губы Архимагистра мягко разжимаются и голова бессильно падает на грудь."

                show archMaster concussion
                with dissolve

                "Ты подходишь ближе к заключенной и приподнимаешь её голову.
                Бедняжка хотела предупредить тебя о чём-то, но силы совсем
                оставили её измученное тело."

                menu:

                    "Оставить пленницу в покое.":
                        jump dungeonCastleArchMasterDialogue3

                    "Попытаться привести Архимагистра в чувство, ударив несколько раз её по щекам":
                        jump dungeonCastleArchMasterDialogue3

                    "Провести большим пальцем по верхней губе Архимагистра.":
                        jump dungeonCastleArchMasterDialogue3
                
                label dungeonCastleArchMasterDialogue3:

                    show lieutenant idle
                    with dissolve

                    "В темницу заходит ваш поручик."

                    lieut "Сэр, я здесь чтобы сообщить вам о том, что всё готово к нашему путешествию."

                    "Ты отпускаешь голову Архимагистра и благодаришь поручика. Что
                    она хотела сказать? Неужели Монарх и правда пользуются тобой
                    как фигурой на шахматной доске. Тебе не хочется в это верить.
                    После стольких лет, проведённых в допросах предателей, лжецов,
                    изменников и еретиков твоя душа зачерствела. В конце концов,
                    твоя дружба с Монархом единственная светлая вещь в твоей жизни."

                    scene bg prologueEnd
                    with fade
                    
                    "Слуга учтиво открывает дверцу кабинки экипажа перед тобой. Ты
                    устраиваешься поудобнее на лавочке. В дороге будет достаточно
                    времени, чтобы ознакомиться со всеми имеющимися деталями. Кучер
                    издаёт громкое \"Тррруу!\" и щелчком поводьев отправляет лошадей
                    в лёгкий голоп. Прямо за твоим экипажем верхом на лошадях едут
                    твои верные помощники: Поручик и Архивариус. Вместе вы
                    распутали добрую сотню дел и теперь вам вновь предстояла
                    непростая работёнка…"

                    jump chapterOne

