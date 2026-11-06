# الحلقة 0.2 — تجهيز البيئة: Terminal و Linux (سكربت للمراجعة)

- الموضوع (من خطة الدورة): CLI Basics, Navigation, Permissions, Environment Setup — التطبيق: إعداد بيئة التطوير والطرفية بالكامل
- يكمل من 0.1: سؤال نهاية الحلقة "وين نكتب الكود اللي يرسل هالطلبات؟" + وعد "نفك عقدة الشاشة السوداء"
- عدد كلمات التعليق: 1560 — المدة التقديرية: ~12.6 دقيقة (130 كلمة/دقيقة + الشعار والانتقالات)
- قواعد الشاشة: كل نافذة Terminal / شات سوداء عامة بدون أي شعار أو اسم برنامج؛ الأوامر تنكتب حرفاً حرفاً (~25 حرف/ثانية)، ثم يطلع المخرج سطر سطر بعد 0.3 ثانية؛ الموجّه دائماً aziz@laptop. علامات ✓ و ✕ تُرسم كأشكال لا كخط (Cairo ما يدعمها).


## 1. ربط بالحلقة 0.1 (ملخص سريع)  `~0:00` (45 كلمة)

**التعليق:**

هلا والله! في الحلقة الماضية فهمنا كيف يشتغل الإنترنت: المتصفح، الـ Client، يرسل Request، والسيرفر يرد بـ Response فيه Status Code. شفنا الـ DNS يحوّل اسم الموقع لرقم IP، وفتحنا Chrome DevTools وشفنا الطلبات بعيوننا. وختمنا بسؤال: وين نكتب الكود اللي يرسل هالطلبات؟ اليوم نجاوب.

**[VISUAL]**

```
شاشة مقسومة سريعة (مونتاج 3 لقطات من الحلقة 0.1، كل لقطة ثانيتين بإطار سماوي):
1) حزمة Request تطلع من أيقونة متصفح عامة (لابتوب) إلى أيقونة سيرفر، وترجع حزمة Response عليها شارة خضراء "200 OK".
2) مخطط DNS: "youtube.com" يتحول بحركة قلب إلى "142.250.185.78".
3) لوحة شبيهة بالـ DevTools (بدون شعار): صف "GET  /  200".
عند "وين نكتب الكود؟": الثلاث لقطات تصغر وتنسحب، وتطلع شاشة سوداء فاضية فيها مؤشر أبيض يومض █ ونص كبير فوقها: "الحلقة 0.2: Terminal و Linux".
```

## [INTRO] شعار القناة المتحرك  `~0:22` (0 كلمة)

**التعليق:**

(بدون تعليق؛ نفس intro_anim.mp4 بدون تعديل)

**[VISUAL]**

```
intro_anim.mp4 كما هو (5 ثواني).
```

## 2. نرد على أسئلتكم من الحلقة 0.1  `~0:27` (119 كلمة)

**التعليق:**

قبل لا نبدأ، سألتكم ثلاث أسئلة، وشفت أجوبتكم في التعليقات، الله يعطيكم العافية.
السؤال الأول: لو طلع لك خطأ خمسمية، المشكلة منك ولا من السيرفر؟ الجواب: من السيرفر. أي رقم يبدأ بخمسة يعني السيرفر نفسه تعطّل، وأنت طلبك سليم. جرّب بعد شوي، أو بلّغ صاحب الموقع.
السؤال الثاني: وش الـ Method اللي تحذف فيها تغريدة؟ الـ DELETE. وانتبه، بعض المواقع عملياً تستخدم POST للحذف، بس المعنى القياسي في الـ REST هو DELETE.
السؤال الثالث: كم طلب طلع لك في DevTools؟ الأرقام كانت تتراوح بين عشرين طلب وأكثر من ثلاثمية! ليش؟ لأن الصفحة الوحدة تطلب الصور، والخطوط، والسكربتات، والإعلانات، كل وحدة بطلب مستقل. وعلى فكرة، بعضكم كتب أرقام كبيرة جداً، وهذا طبيعي في المواقع الإخبارية والمتاجر لأنها مليانة صور وإعلانات.

**[VISUAL]**

```
خلفية الكحلي. بطاقة "سؤال 1" تنزلق من اليمين، والسؤال مكتوب عليها. يظهر مقياس بسهمين: "منك (4xx)" برتقالي ↔ "من السيرفر (5xx)" أحمر؛ السهم يميل إلى 5xx وتطلع شارة "500 Internal Server Error" مع أيقونة سيرفر يطلع منها دخان كرتوني.
بطاقة "سؤال 2": أربع أزرار GET / POST / PUT / DELETE، المؤشر يضغط DELETE فيتحول أحمر، وتغريدة عامة (مستطيل رمادي، بدون شعار) تتفتت وتختفي. سطر صغير تحت: "عملياً: بعض المواقع تستخدم POST".
بطاقة "سؤال 3": لوحة شبيهة بالـ Network تنزل منها صفوف بسرعة، وعداد في الزاوية يعدّ من 0 إلى 312 مع تسميات صفوف: document, script, font, image, xhr. شريط أسفل: "312 requests".
```

## 3. ليش الشاشة السوداء؟  `~1:23` (117 كلمة)

**التعليق:**

طيب، خلنا نبدأ. هذي الشاشة السوداء اللي يخاف منها الكل؟ اسمها Terminal، أو الطرفية. وهي ببساطة طريقة تكلم فيها جهازك بالكتابة بدل الماوس. بدل ما تفتح مجلد بالضغط، تكتب أمر، والجهاز ينفذه فوراً. والبرنامج اللي يفهم أوامرك ويترجمها للنظام اسمه الـ Shell، والمشهور فيه Bash أو Zsh. ليش نتعلمه؟ لأن السيرفرات اللي بنرفع عليها تطبيقات الـ AI غالباً Linux، وما فيها شاشة ولا ماوس. كل شي بالأوامر. وأغلب أدوات الذكاء الاصطناعي، من تثبيت المكتبات إلى تشغيل النماذج، تبدأ بأمر في الـ Terminal. يعني إذا تبي تصير AI Engineer، لازم تصاحب هالشاشة. والخبر الحلو؟ ما تحتاج تحفظ مية أمر، عشرة أوامر تكفيك تسعين بالمية من الشغل، وبنهاية الحلقة بيكون عندك كل اللي تحتاجه من الـ Terminal للدورة كلها.

**[VISUAL]**

```
يسار: نافذة مجلدات رسومية عامة، المؤشر يضغط ضغطتين على مجلد. يمين: نافذة Terminal سوداء (شريط علوي فيه 3 نقاط رمادية فقط، بدون أي اسم برنامج).
عند "تكتب أمر": يكتب حرفاً حرفاً:
  aziz@laptop:~$ ls
ثم يطلع فوراً:
  Desktop  Documents  Downloads  Pictures
عند "الـ Shell": سهم متحرك من لوحة مفاتيح ← فقاعة "Shell (Bash / Zsh)" ← شريحة "نظام التشغيل".
عند "السيرفرات Linux": رف سيرفرات يضوي، وفوق كل سيرفر شارة "Linux"، وشاشة الماوس عليها علامة ✕ (تُرسم كخط، بدون إيموجي).
```

## 4. تجهيز البيئة: ويندوز وماك ولينكس  `~2:19` (65 كلمة)

**التعليق:**

أول خطوة: نجهز البيئة. لو جهازك Mac أو Linux، مبروك، الـ Terminal موجود جاهز، ابحث عن Terminal وافتحه. لو Windows، نثبّت الـ WSL، يعني Linux كامل داخل الويندوز. افتح PowerShell كمسؤول، Run as Administrator، واكتب: wsl --install. أعد تشغيل الجهاز، وبيطلب منك اسم مستخدم وكلمة مرور. وانتبه، وأنت تكتب كلمة المرور ما بيطلع شي على الشاشة، لا نجوم ولا نقاط، وهذا طبيعي، كمّل واضغط Enter.

**[VISUAL]**

```
ثلاث بطاقات أنظمة (رسوم عامة بدون شعارات: مربعات بأسماء نصية "Windows" "macOS" "Linux"). بطاقتا macOS وLinux تطلع عليهما علامة صح خضراء ونص "جاهز".
بطاقة Windows تتكبر وتتحول إلى نافذة Terminal زرقاء داكنة عنوانها "Administrator". يكتب:
  PS C:\> wsl --install
مخرج يظهر سطر سطر:
  Installing: Virtual Machine Platform
  Installing: Windows Subsystem for Linux
  Installing: Ubuntu
  The requested operation is successful. Changes will not be effective until the system is rebooted.
أيقونة إعادة تشغيل تدور. بعدها نافذة سوداء:
  Enter new UNIX username: aziz
  New password:
عند "ما بيطلع شي": المؤشر يومض مكانه وفوقه عدسة مكبرة + نص "طبيعي، كمّل ✓" (علامة الصح تُرسم كخط).
```

## 5. أول أوامر: وين أنا؟ ووش عندي؟  `~2:50` (98 كلمة)

**التعليق:**

الحين، أهم ثلاث أوامر بتستخدمها كل يوم. الأول: pwd، يعني Print Working Directory، يقول لك أنت وين الحين بالضبط. الثاني: ls، يعرض لك وش موجود في المجلد. والثالث: cd، يعني Change Directory، تنتقل فيه بين المجلدات. تخيلها مثل خريطة مول: pwd تقول لك "أنت هنا"، ls توريك المحلات حولك، و cd تمشي فيها. ولو تبي ترجع خطوة لورا، اكتب cd نقطتين. ومعلومة مهمة: فيه مسار كامل يبدأ بالشرطة، مثل /home/aziz/Documents، يشتغل من أي مكان. وفيه مسار نسبي، مثل Documents بس، يعتمد على مكانك الحين. ورمز الموجة ~ معناه مجلدك الرئيسي، يعني cd ~ ترجعك للبيت من أي مكان.

**[VISUAL]**

```
Terminal أسود يغطي يمين الشاشة، ويسارها شجرة مجلدات متحركة (home ← aziz ← Desktop, Documents, Downloads) مع دبوس سماوي "أنت هنا".
يكتب حرفاً حرفاً، وكل أمر ينفذ:
  aziz@laptop:~$ pwd
  /home/aziz
(الدبوس ينبض على aziz)
  aziz@laptop:~$ ls
  Desktop  Documents  Downloads
(الثلاث مجلدات في الشجرة تضوي واحد واحد)
  aziz@laptop:~$ cd Documents
  aziz@laptop:~/Documents$ pwd
  /home/aziz/Documents
(الدبوس يتنقل لـ Documents بحركة قفزة)
  aziz@laptop:~/Documents$ cd ..
  aziz@laptop:~$
(الدبوس يرجع لـ aziz)
عند "خريطة مول": الشجرة تتحول لحظياً لخريطة مول بسيطة: دبوس "أنت هنا" = pwd، محلات = ls، خطوات = cd.
عند "المسار الكامل": سطر  /home/aziz/Documents  تنفصل أجزاؤه وتتلون؛ ثم  aziz@laptop:~/Documents$ cd ~  والدبوس يطير للبيت (أيقونة بيت فوق aziz).
```

## 6. نبني مجلد مشروعنا  `~3:37` (53 كلمة)

**التعليق:**

يلا نبني مجلد الدورة اللي بنشتغل فيه طول الموسم. اكتب: mkdir ai-course، يعني Make Directory. ادخل عليه بـ cd. بعدين touch notes.txt يسوي لك ملف فاضي. ونكتب فيه سطر بـ echo، والعلامة الأكبر من تحط الكلام داخل الملف. و cat يعرض لك محتواه. شفت؟ سوينا مجلد وملف وكتبنا فيه، بدون ولا ضغطة ماوس.

**[VISUAL]**

```
Terminal في المنتصف، وتحته نافذة مجلدات صغيرة تتحدث مباشرة مع كل أمر.
  aziz@laptop:~$ mkdir ai-course
(مجلد جديد "ai-course" يطلع بحركة pop في النافذة)
  aziz@laptop:~$ cd ai-course
  aziz@laptop:~/ai-course$ touch notes.txt
(ملف فاضي "notes.txt" يطلع داخل المجلد)
  aziz@laptop:~/ai-course$ echo "Episode 0.2: Terminal" > notes.txt
(سطر نص يطير من الأمر ويدخل الملف، الملف يصير له خطوط)
  aziz@laptop:~/ai-course$ cat notes.txt
  Episode 0.2: Terminal
  aziz@laptop:~/ai-course$ ls
  notes.txt
عند "بدون ولا ضغطة ماوس": أيقونة ماوس رمادية مشطوبة بخط.
```

## 7. نسخ ونقل وحذف (وتحذير مهم)  `~4:03` (52 كلمة)

**التعليق:**

الحين cp للنسخ، و mv للنقل أو تغيير الاسم، و rm للحذف. بس انتبه هنا، وهذي أهم نقطة في الحلقة: rm ما يرسل الملف لسلة المحذوفات، يحذفه نهائياً! وفيه أمر مشهور، rm -rf، يحذف مجلد كامل بكل اللي فيه بدون ما يسألك. عشان كذا، قبل أي rm، اكتب pwd وتأكد أنت وين.

**[VISUAL]**

```
  aziz@laptop:~/ai-course$ cp notes.txt backup.txt
  aziz@laptop:~/ai-course$ ls
  backup.txt  notes.txt
(نسخة من الملف تنفصل عنه بحركة)
  aziz@laptop:~/ai-course$ mv backup.txt old.txt
  aziz@laptop:~/ai-course$ ls
  notes.txt  old.txt
(اسم الملف يتبدل حرفاً حرفاً)
  aziz@laptop:~/ai-course$ rm old.txt
  aziz@laptop:~/ai-course$ ls
  notes.txt
(الملف يتحول جزيئات ويختفي، وأيقونة سلة محذوفات جنبه تبقى فاضية مع نص "مو هنا!")
عند rm -rf: الشاشة يحيط فيها إطار أحمر يومض، ويكتب الأمر بلون رمادي باهت بدون تنفيذ: rm -rf ai-course ، مع ختم أحمر "لا تجربه عشوائياً". ثم بطاقة قاعدة: "قبل rm ← pwd".
```

## 7ب. نعدّل ملف من داخل الـ Terminal: nano  `~4:28` (67 كلمة)

**التعليق:**

طيب، echo حلو لسطر واحد، بس لو تبي تكتب أكثر؟ نستخدم محرر نصوص داخل الـ Terminal اسمه nano. اكتب nano notes.txt، وبيفتح لك الملف. اكتب اللي تبيه عادي، وتحت بتشوف الاختصارات. عشان تحفظ اضغط Ctrl+O ثم Enter، وعشان تطلع اضغط Ctrl+X. ولا تخاف، الشاشة تحت دايماً تذكرك. وبعدها cat ونشوف إن الكلام انحفظ. وفي الحلقة الجاية بنستخدم VS Code للبرمجة الجدية، بس nano بينقذك كثير على السيرفرات.

**[VISUAL]**

```
  aziz@laptop:~/ai-course$ nano notes.txt
الـ Terminal يتحول لمحرر: شريط علوي "GNU nano  notes.txt"، والسطر الموجود "Episode 0.2: Terminal"، والمؤشر ينزل سطر جديد ويكتب حرفاً حرفاً:
  pwd = where am I
  ls  = what's here
  cd  = move
شريط سفلي: "^O Write Out   ^X Exit   ^K Cut   ^W Where Is" — عند ذكر Ctrl+O يضوي "^O" سماوي، يطلع "File Name to Write: notes.txt" ثم "[ Wrote 4 lines ]"، وعند Ctrl+X يضوي "^X" ويرجع الـ Terminal.
  aziz@laptop:~/ai-course$ cat notes.txt
  Episode 0.2: Terminal
  pwd = where am I
  ls  = what's here
  cd  = move
```

## 8. الصلاحيات: Permission denied  `~5:01` (86 كلمة)

**التعليق:**

طيب، يمكن يطلع لك خطأ اسمه Permission denied. يعني ما عندك صلاحية. في Linux، كل ملف له ثلاث صلاحيات: r قراءة، w كتابة، و x تنفيذ. وتشوفها بـ ls -l. والصلاحيات مقسمة لثلاث مجموعات: صاحب الملف، ومجموعته، وباقي المستخدمين. يعني ممكن ملف تقدر أنت تعدّله، وغيرك بس يقرأه. خلنا نسوي سكربت صغير اسمه hello.sh ونحاول نشغله... رفض! لأنه ما عنده صلاحية تنفيذ. الحل: chmod +x، نعطيه صلاحية التنفيذ، ونشغله مرة ثانية، واشتغل! وفيه sudo، يعني شغّل الأمر كمسؤول. استخدمه بحذر، وبس لما تحتاجه، مثل تثبيت البرامج.

**[VISUAL]**

```
  aziz@laptop:~/ai-course$ echo 'echo "Hala from Aziz Tech SA!"' > hello.sh
(ملف hello.sh يطلع)
  aziz@laptop:~/ai-course$ ./hello.sh
  bash: ./hello.sh: Permission denied
(السطر يطلع أحمر، وقفل كرتوني يقفل على الملف مع صوت "تك")
  aziz@laptop:~/ai-course$ ls -l hello.sh
  -rw-r--r-- 1 aziz aziz 31 Nov 5 10:00 hello.sh
(تكبير على -rw-r--r-- : الحروف تنفصل لثلاث بطاقات r = قراءة، w = كتابة، x = تنفيذ؛ بطاقة x رمادية "ناقصة")
  aziz@laptop:~/ai-course$ chmod +x hello.sh
  aziz@laptop:~/ai-course$ ls -l hello.sh
  -rwxr-xr-x 1 aziz aziz 31 Nov 5 10:00 hello.sh
(بطاقة x تضوي سماوي، والقفل ينفتح)
  aziz@laptop:~/ai-course$ ./hello.sh
  Hala from Aziz Tech SA!
(السطر يطلع أخضر مع لمعة)
عند sudo: شارة "sudo = مسؤول" بتاج بسيط، مع نص صغير "بحذر".
عند "ثلاث مجموعات": rwx | r-x | r-x تنقسم لثلاث خانات بعناوين: المالك، المجموعة، الباقي.
```

## 9. نثبّت أدواتنا  `~5:42` (77 كلمة)

**التعليق:**

الحين نثبت الأدوات اللي بنحتاجها في الدورة. في Linux عندنا مدير حزم اسمه apt، مثل متجر تطبيقات بس بالأوامر. أول شي sudo apt update يحدّث القائمة، بعدين نثبت python3 و git و curl بأمر واحد. ونتأكد إنها تثبتت بـ --version. وتذكر curl؟ هذا يرسل HTTP Request من الـ Terminal نفسه! جرّب curl -I على أي موقع، وبتشوف الـ Status Code والـ Headers، نفس اللي شفناه في DevTools بالحلقة الماضية. يعني هنا بالضبط نكتب الكود اللي يرسل الطلبات.

**[VISUAL]**

```
  aziz@laptop:~$ sudo apt update
  [sudo] password for aziz:
  Reading package lists... Done
  aziz@laptop:~$ sudo apt install -y python3 git curl
  Reading package lists... Done
  Setting up python3 ...
  Setting up git ...
  Setting up curl ...
(شريط تقدم سماوي يمتلئ، وثلاث أيقونات صناديق عامة "python3" "git" "curl" تنزل في رف)
  aziz@laptop:~$ python3 --version
  Python 3.12.3
  aziz@laptop:~$ git --version
  git version 2.43.0
(علامة صح خضراء بجانب كل سطر)
عند curl: يكتب
  aziz@laptop:~$ curl -I https://example.com
  HTTP/2 200
  content-type: text/html
  content-length: 1256
(حزمة Request تطير من الـ Terminal لأيقونة سيرفر وترجع Response — نفس رسمة الحلقة 0.1 — والسطر "HTTP/2 200" يتلون أخضر ويتربط بخط منقط ببطاقة "200 OK" من الحلقة الماضية)
```

## 9ب. نجمع كل شي: سكربت يجهز المشروع  `~6:19` (75 كلمة)

**التعليق:**

خلنا نجمع كل اللي تعلمناه في سكربت واحد يجهز لك مشروع الدورة كامل بضغطة. نفتح nano setup.sh، ونكتب فيه: سطر يقول للجهاز إن هذا سكربت Bash، بعدين mkdir -p يسوي مجلدات المشروع كلها مرة وحدة، ونطبع رسالة إن كل شي جاهز، ونطلع نسخة الـ Python. نحفظ ونطلع، نعطيه صلاحية تنفيذ بـ chmod، ونشغله. وشوف! المجلدات انبنت، والرسالة طلعت. هذا اللي يسمونه Automation، وهو قلب شغل الـ AI Engineer: أي شي تكرره، خلّ الجهاز يسويه بدالك.

**[VISUAL]**

```
  aziz@laptop:~/ai-course$ nano setup.sh
داخل المحرر، يكتب حرفاً حرفاً:
  #!/bin/bash
  mkdir -p projects/week1 data notes
  echo "Project folders ready!"
  python3 --version
(Ctrl+O ← "[ Wrote 4 lines ]" ← Ctrl+X)
  aziz@laptop:~/ai-course$ chmod +x setup.sh
  aziz@laptop:~/ai-course$ ./setup.sh
  Project folders ready!
  Python 3.12.3
  aziz@laptop:~/ai-course$ ls
  data  hello.sh  notes  notes.txt  projects  setup.sh
(بجانب الـ Terminal، شجرة المجلدات تنبني فرع فرع: data, notes, projects ← week1، مع شرارة سماوية على كل مجلد)
عند "Automation": ترس كبير يدور ونص "كرّرت؟ خلّ السكربت يسويه".
```

## 9ج. نكتب ونقرأ ملفات كبيرة: > و >> و head و tail و less  `~6:55` (87 كلمة)

**التعليق:**

طيب، تذكر العلامة الأكبر من؟ هذي اسمها Redirection. علامة وحدة > تكتب فوق الملف وتمسح القديم، وعلامتين >> تضيف سطر في آخره بدون ما تمسح شي. خلنا نسوي ملف سجل صغير لسيرفر، فيه طلبات وأرقام Status Code مثل اللي شفناها بالحلقة الماضية. والحين، تخيل الملف فيه مليون سطر، cat بيغرقك! عشان كذا عندنا head يعرض أول الأسطر، و tail يعرض آخرها، و tail -f يتابع الملف وهو يتحدث مباشرة، وهذا اللي يسويه المبرمجين وهم يراقبون السيرفر. و less يفتح الملف صفحة صفحة، تنزل بالأسهم، وتطلع بحرف q.

**[VISUAL]**

```
  aziz@laptop:~/ai-course$ echo "GET /home 200" > server.log
  aziz@laptop:~/ai-course$ echo "GET /login 200" >> server.log
  aziz@laptop:~/ai-course$ echo "GET /old-page 404" >> server.log
  aziz@laptop:~/ai-course$ echo "POST /api 500" >> server.log
  aziz@laptop:~/ai-course$ echo "GET /about 404" >> server.log
(كل سطر يطير من الأمر وينزل تحت اللي قبله في أيقونة ملف server.log؛ عند > الأولى ممسحة صغيرة تمسح الملف قبل الكتابة، وعند >> علامة + خضراء)
  aziz@laptop:~/ai-course$ head -2 server.log
  GET /home 200
  GET /login 200
  aziz@laptop:~/ai-course$ tail -1 server.log
  GET /about 404
(الملف يتمدد لمستند طويل جداً مع عداد "1,000,000 سطر"؛ head يضوي أعلاه و tail يضوي أسفله)
  aziz@laptop:~/ai-course$ less server.log
(الشاشة تتحول لعارض صفحات، شريط سفلي "server.log (END)"، ضغطة q ويرجع الـ Terminal)
```

## 9د. نبحث ونربط الأوامر: grep والـ Pipes  `~7:37` (89 كلمة)

**التعليق:**

الحين أقوى حركة في الحلقة. grep يدور لك على كلمة داخل الملفات، مثل Ctrl+F بس للـ Terminal. نبي كل الطلبات اللي رجعت 404؟ grep 404 server.log، وخلاص. والسحر الحقيقي في الـ Pipe، الخط العمودي هذا |. هو ياخذ مخرج أمر ويعطيه للأمر اللي بعده، كأنها سلسلة مصنع. cat server.log | grep 404 | wc -l، يعني اعرض الملف، فلتر الـ 404، وعدّها: صفحتين ضايعة. و ls | wc -l يعد ملفاتك. ونسيت أمر كتبته أمس؟ history | grep chmod ويطلع لك. بأوامر صغيرة مربوطة ببعض، تسوي شغل برنامج كامل.

**[VISUAL]**

```
  aziz@laptop:~/ai-course$ grep 404 server.log
  GET /old-page 404
  GET /about 404
(كلمة 404 تتلون أحمر داخل كل سطر)
  aziz@laptop:~/ai-course$ cat server.log | grep 404 | wc -l
  2
(رسمة خط مصنع: 5 أسطر تطلع من cat، تدخل أنبوب | إلى فلتر grep فيطلع سطرين، تدخل أنبوب | إلى عداد wc -l فيطلع الرقم 2)
  aziz@laptop:~/ai-course$ ls | wc -l
  7
  aziz@laptop:~/ai-course$ history | grep chmod
     41  chmod +x hello.sh
     57  chmod +x setup.sh
(بطاقة: "| = خذ المخرج وأعطه للي بعده")
```

## 9هـ. البرامج الشغالة: Processes  `~8:19` (99 كلمة)

**التعليق:**

أي برنامج يشتغل في جهازك اسمه Process، وله رقم خاص اسمه PID. خلنا نشغل سيرفر حقيقي من جهازك بأمر واحد من Python: python3 -m http.server. شوف! السيرفر شغال وينتظر طلبات، والـ Terminal صار مشغول. نوقفه بـ Ctrl+C. طيب لو أبي أشغله وأكمل شغلي؟ أحط & في آخر الأمر، فيشتغل في الخلفية. والحين نرسل له Request بـ curl، ويرد علينا 200 OK. صرنا السيرفر والـ Client في نفس الوقت! ونشوف البرامج الشغالة بـ ps، أو top اللي يعرضها مباشرة مع استهلاك المعالج والذاكرة. وعشان نوقف اللي في الخلفية: kill ورقم الـ PID. هذا اللي بنسويه مع كل تطبيق AI نشغله.

**[VISUAL]**

```
  aziz@laptop:~/ai-course$ python3 -m http.server 8000
  Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
(المؤشر يختفي، وأيقونة سيرفر صغيرة تضوي "شغال"؛ ثم ضغطة Ctrl+C)
  ^C
  Keyboard interrupt received, exiting.
  aziz@laptop:~/ai-course$ python3 -m http.server 8000 &
  [1] 4821
(السيرفر ينزلق لرف "الخلفية" والموجّه يرجع)
  aziz@laptop:~/ai-course$ curl -I http://localhost:8000
  HTTP/1.0 200 OK
  Server: SimpleHTTP/0.6 Python/3.12.3
(حزمة Request تطلع وترجع داخل نفس اللابتوب، بنفس رسمة الحلقة 0.1)
  aziz@laptop:~/ai-course$ ps
    PID TTY          TIME CMD
   4790 pts/0    00:00:00 bash
   4821 pts/0    00:00:00 python3
   4830 pts/0    00:00:00 ps
(سطر 4821 يضوي)
  aziz@laptop:~/ai-course$ top
(لقطة سريعة لجدول حي: PID, USER, %CPU, %MEM, COMMAND والأرقام تتغير؛ q للخروج)
  aziz@laptop:~/ai-course$ kill 4821
  [1]+  Terminated              python3 -m http.server 8000
(أيقونة السيرفر تنطفي)
```

## 10. متغيرات البيئة والـ PATH  `~9:07` (71 كلمة)

**التعليق:**

وآخر مفهوم مهم: متغيرات البيئة، Environment Variables. هذي قيم يحفظها الـ Shell ويستخدمها أي برنامج. مثلاً echo $HOME يطلع لك مجلدك. وأهمها الـ PATH، قائمة المجلدات اللي يدور فيها الجهاز عن أي أمر تكتبه. عشان كذا لما تكتب python3، الجهاز يعرف وينه، و which python3 يقول لك وينه بالضبط. ونقدر نسوي متغير بنفسنا بـ export. وهذا بالضبط اللي بنستخدمه بعدين عشان نخزن مفاتيح الـ API بأمان، بدل ما نكتبها داخل الكود.

**[VISUAL]**

```
  aziz@laptop:~$ echo $HOME
  /home/aziz
  aziz@laptop:~$ echo $PATH
  /usr/local/bin:/usr/bin:/bin
(الـ PATH ينقسم عند النقطتين لثلاث بطاقات مجلدات)
  aziz@laptop:~$ which python3
  /usr/bin/python3
(عدسة تمر على البطاقات وتوقف عند /usr/bin وتلقى python3 داخلها)
  aziz@laptop:~$ export COURSE="AI Engineer"
  aziz@laptop:~$ echo $COURSE
  AI Engineer
(صندوق صغير عليه ملصق COURSE تنحط فيه كلمة "AI Engineer")
عند "مفاتيح الـ API": صندوق عليه ملصق API_KEY وقيمته مخفية "sk-******" بقفل، مع نص "الحلقة 0.9".
```

## 10ب. ssh: نتحكم بسيرفر من بعيد  `~9:41` (84 كلمة)

**التعليق:**

طيب، كل هذا في جهازك. بس تطبيقك بالأخير بيعيش على سيرفر في مكان ثاني من العالم، كيف تدخله؟ بـ ssh، يعني Secure Shell. تكتب ssh وبعده اسم المستخدم، علامة @، وعنوان السيرفر، وتلقى نفسك داخل Terminal السيرفر، وكل الأوامر اللي تعلمناها اليوم تشتغل هناك بالضبط. وهذا اللي بنستخدمه لما نرفع مشاريعنا للعالم. وبدل كلمة المرور كل مرة، نسوي مفتاح بـ ssh-keygen: مفتاح خاص يبقى عندك وما تعطيه أحد، ومفتاح عام تعطيه للسيرفر. وهذا نفس المفتاح اللي بنربط فيه جهازك بـ GitHub في الحلقة 0.6.

**[VISUAL]**

```
  aziz@laptop:~$ ssh aziz@203.0.113.10
  aziz@203.0.113.10's password:
  Welcome to Ubuntu 24.04 LTS
  aziz@server:~$ pwd
  /home/aziz
  aziz@server:~$ exit
  logout
  Connection to 203.0.113.10 closed.
(نفق مضيء يمتد من أيقونة اللابتوب إلى سيرفر بعيد على خريطة عامة، والموجّه يتحول من laptop إلى server ثم يرجع)
  aziz@laptop:~$ ssh-keygen -t ed25519
  Generating public/private ed25519 key pair.
  Enter file in which to save the key (/home/aziz/.ssh/id_ed25519):
  Your identification has been saved in /home/aziz/.ssh/id_ed25519
  Your public key has been saved in /home/aziz/.ssh/id_ed25519.pub
(مفتاحين يطلعون: مفتاح ذهبي بقفل "id_ed25519 خاص - لا تشاركه"، ومفتاح فضي "id_ed25519.pub عام" يطير للسيرفر، وبطاقة صغيرة "الحلقة 0.6: GitHub")
```

## 11. خمس اختصارات توفر عليك ساعات  `~10:21` (53 كلمة)

**التعليق:**

وهدية الحلقة: خمس اختصارات تختصر عليك ساعات. واحد: زر Tab يكمّل اسم الملف أو الأمر بدالك. اثنين: السهم لفوق يرجّع لك الأوامر السابقة. ثلاثة: Ctrl+C يوقف أي أمر علّق. أربعة: clear أو Ctrl+L ينظف الشاشة. وخمسة: أي أمر ما تعرفه، اكتب بعده --help، أو اكتب man وبعده اسم الأمر، ويفتح لك دليله الكامل.

**[VISUAL]**

```
عداد كبير 1/5 ← 5/5، ولوحة مفاتيح عامة تحت الـ Terminal والزر المذكور يضوي سماوي وينضغط:
1) Tab: يكتب "cd ai-c" ثم يضغط Tab فيكمل تلقائياً إلى "cd ai-course/".
2) ↑: الأوامر السابقة تطلع واحد بعد الثاني في السطر (ls ← pwd ← mkdir ai-course).
3) Ctrl+C: أمر  ping example.com  يطبع أسطر "64 bytes from ..." بلا توقف، ثم يطلع  ^C  ويتوقف.
4) Ctrl+L: الشاشة المليانة تنمسح بحركة مسح لفوق.
5) --help: يكتب  ls --help  فيطلع:
  Usage: ls [OPTION]... [FILE]...
  List information about the FILEs (the current directory by default).
بالنهاية بطاقة ملخص فيها الخمسة.
  aziz@laptop:~$ man grep
  GREP(1)          User Commands          GREP(1)
  NAME
         grep - print lines that match patterns
(q للخروج)
```

## 11ب. عدة الدورة كاملة: وين بنستخدم كل هذا؟  `~10:47` (78 كلمة)

**التعليق:**

وقبل لا نختم، خلني أوريك ليش هذي الحلقة مهمة. كل أمر تعلمناه اليوم بنستخدمه في كل حلقة جاية. في 0.3 و 0.4 بنشغل ملفات Python بـ python3. في 0.5 بنثبت المكتبات بـ pip، ونسوي بيئة معزولة لكل مشروع بـ python3 -m venv، ونفعّلها بأمر source. وفي 0.6 نستخدم git مع مفتاح الـ ssh. ومجلدات مثل .venv و .git مخفية، يعني ls العادي ما يوريها، تشوفها بـ ls -a. يعني الـ Terminal مو درس وخلص، هو بيتك طول الدورة.

**[VISUAL]**

```
خريطة طريق أفقية بأربع محطات تضوي بالترتيب، وتحت كل محطة Terminal صغير يكتب أمرها:
0.3-0.4 Python:   aziz@laptop:~/ai-course$ python3 calc.py
0.5 pip و venv:   aziz@laptop:~/ai-course$ python3 -m venv .venv
                  aziz@laptop:~/ai-course$ source .venv/bin/activate
                  (.venv) aziz@laptop:~/ai-course$ pip install requests
0.6 Git:          aziz@laptop:~/ai-course$ git init
                  Initialized empty Git repository in /home/aziz/ai-course/.git/
                  aziz@laptop:~/ai-course$ ls -a
                  .  ..  .git  .venv  data  hello.sh  notes  notes.txt  projects  server.log  setup.sh
النشر:            aziz@laptop:~$ ssh aziz@server
فوق الخريطة نص: "Terminal = بيتك طول الدورة".
```

## 12. أسئلة لكم في التعليقات  `~11:25` (58 كلمة)

**التعليق:**

قبل لا نختم، عندي لكم ثلاث أسئلة، أبي أشوف أجوبتكم في التعليقات. السؤال الأول: اكتب أمر واحد بالـ Pipe يعد كم ملف في مجلدك. السؤال الثاني: لو شغلت سكربت وطلع لك Permission denied، وش الأمر اللي يحل المشكلة؟ والسؤال الثالث: شغلت سيرفر في الخلفية ورقمه 4821، كيف توقفه؟ اكتب جوابك في التعليقات، وأنا برد عليكم في الحلقة الجاية.

**[VISUAL]**

```
نفس قالب أسئلة الحلقة 0.1: ثلاث بطاقات مرقمة، كل وحدة فيها Terminal صغير بسطر ناقص:
1) aziz@laptop:~$ ??? | ???      ومخرجه 7
2) bash: ./hello.sh: Permission denied   ثم   aziz@laptop:~$ ??? hello.sh
3) [1] 4821   ثم   aziz@laptop:~$ ??? 4821   ثم   [1]+  Terminated
آخرها فقاعة تعليق تنبض ونص "اكتب جوابك في التعليقات".
```

## 13. وش الحلقة الجاية؟ (0.3)  `~11:53` (49 كلمة)

**التعليق:**

طيب، البيئة جاهزة، والـ Terminal صار صاحبك. في الحلقة الجاية، نكتب أول سطر Python! نتعرف على أنواع البيانات، و if و else، والـ Loops، ونجهز VS Code، ونبني حاسبة كاملة تشتغل في الـ Terminal، بأقل من عشرة أسطر. وصدقني، بتنبسط وأنت تشوف كودك يشتغل قدامك لأول مرة، فلا تفوتها.

**[VISUAL]**

```
الـ Terminal يكتب:  aziz@laptop:~/ai-course$ python3 calc.py
ثم تطلع لمحة (Teaser) من الحلقة الجاية:
  Enter first number: 8
  Enter operator (+ - * /): *
  Enter second number: 5
  Result: 40
فوقه بطاقة: "الحلقة 0.3: أساسيات Python 1" وتحتها شارات: Data Types · if/else · Loops · VS Code، ونص "حاسبة كاملة بأقل من 10 أسطر".
```

## 14. الخاتمة  `~12:17` (38 كلمة)

**التعليق:**

وإذا وصلت لهنا، فأنت رسمياً كتبت أوامرك الأولى في Linux، الله يعطيك العافية! لا تنسى تشترك في قناة عزيز تِك SA، وتفعّل الجرس عشان توصلك الحلقة الجاية أول ما تنزل، وحط لايك لو استفدت. ونشوفكم في الحلقة الجاية!

**[VISUAL]**

```
outro_anim.mp4 (نفس شعار البداية المتحرك + اسم القناة "Aziz Tech SA / عزيز للتقنية")، وفوقه أزرار متحركة: زر "اشتراك" ينضغط ويتحول إلى "مشترك"، أيقونة الجرس تهتز، وزر لايك ينضغط. تحتها رابط القناة youtube.com/channel/UC-Y8R5wOzkm_ynaQZISDdbw وبطاقة "الحلقة التالية: 0.3 أساسيات Python 1".
```
