def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
<div class="concept">
    <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
    </div>
    <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
    </div>
</div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

JD_LIST_OF_CONCEPTS = [ ['World Wide Web', 'The World Wide Web is a collection of HTML documents. HTML stands for Hyper Text Markup Language. The Web has been around since the 1990s and has 30 billion pages. HTML represents a majority of the documents on the Web. Other documents or files found on the web include Microsoft Word, PDF, plain text, images, videos and music.'],
                        ['Major Pieces', 'Components of the web include: HTTP, Servers, Internet and Browser.  For a detailed explanation of the web components, go to <a href="http://www.udacity.com/course/viewer/#!/c-nd000/l-3873828673/e-48329854/m-48299873">the Video</a>. HTTP – the main protocol of the web. Servers – computers that host the files that make up the web.  Internet – the world’s largest computer network. Browser – a program that runs on your computer to display files found on the web.'],
                        ['HTML', 'Hyper Text Markup Language documents makes up most of the documents you see on the web.  HTML is made up of: text content (what you see), markup (what it looks like), reference to other documents (images, videos, etc.), and links to other pages.'],
                        ['HTML Markup', 'Tag: an HTML tag is always contained within angled brackets.  Most tags have an opening tag and a closing tag.  Some tags do not require a closing tag. Element: an HTML element refers to everything within a set of opening and closing tags.'],
                        ['Computers Are Stupid', 'Programmers need to write code exactly the way a computer understands (write in correct syntax).'],
                        ['HTML Attributes', 'Attribute: this is a property of an HTML element.  For a detailed explanation of attributes go to <a href="https://www.udacity.com/course/viewer/#!/c-nd000/l-3873828673/e-48508417/m-48723411">the Video</a>.'],
                        ['Images', 'Images are void tags which means there is no content and does not need a closing tag.  For a detailed explanation of images go to <a href="https://www.udacity.com/course/viewer/#!/c-nd000/l-3873828673/m-48744041">the Video</a>.'],
                        ['Whitespace', 'To get text on multiple lines, you can use void tags and closing tags.  For a detailed explanation of line break tabs, go to <a href="https://www.udacity.com/course/viewer/#!/c-nd000/l-3873828673/e-48666064/m-48678767">the Video</a>.'],
                        ['Span and Div', 'Blocks make an invisible box around what you are doing that can be edited and reviewed as a whole. Inline makes just an alteration inside an already existing block. <a href="https://www.udacity.com/course/viewer/#!/c-nd000/l-3873828673/e-48756004/m-48605783">See Video</a> on inline and block elements.'],
                        ['Tree Structure', 'Tree like structure consists of sideways trianges with open and close tags, span and elements.  You can click on the elements to get font and border size information.'],
                        ['HTML/CSS/DOM', 'HTML is the language of the web and has syntax and rules.  HTML is writted in a document. CSS is the style that lets you use syntax and rules to change how elements look on the page (font, color, background, borders, position). Boxes are defined wih div tags.'],
                        ['CSS', 'CSS stands for cascading style sheets. These style sheets are what is used to determining how a page looks on the internet. You can control virtually every aspect of a page if you know the correct CSS to use. Think of it as the decorations or the style of your house.'],
                        ['Avoiding Repitition', 'Consistency is another very good reason to avoid repetition when writing HTML code. If you want to give a document or a series of documents the same feel, then they must be coded the same. This is best done by assigning specific "classes" to each part of the document. By having different "classes" for each part of the document, you only have to change the class file in your CSS to make changes throughout the entire document.'],
                        ['Computer', 'A computer is a machine that can be programmed.  Computers can only do what a program tells them to do. A program tells the computer what to do in a precise sequence of steps.'],
                        ['Computer Program and Computer Science', 'A computer program is a sequence of instructions written to perform a specific task with a computer.  Computer science deals with the theoretical foundations of information and computation, together with practical techniques for the implementation and application of these foundations.  Programming is the core of computer science.'],
                        ['Web Page and Web Browser', 'A web page is really just a chunk of text that comes from the Internet into your Web browser. A web page is a web document that is suitable for a web browser.  The web browser is the software program that accesses the web document and follows links to find pages in the document and displays the contents on the user\'s computer.  The web browser becomes the editor for coding using programming languages such as Python. You can run Python in the web browser.'],
                        ['Python', 'Python is called an interpreter.  It runs out programs, it interprets them, executes the programs that we wrote in Python language by running a program in a language into the computer can understand directly.  Procedural thinking is to follow the instructions in your code.  An example of Abstract thinking is seeing a Python program, Python interpreter, and a web browser as different versions of the same thing (a computer program). If you try to use code that is not in the Python dictionary it will return a syntax error. Python has a grammar to define what strings are in the language. It is stricter than the English language or other natural languages. With Python the code needs to match the Python grammar exactly.'],
                        ['Variables in Python', 'Variables give programmers a way to give names to values. If jd_variable is a variable with a value of 5, then the following code would print out  10:  print jd_variable + jd_variable.'],
                        ['Assigning a value to a variable', 'We can assign the value 5 to the variable jd_variable by writing code like this:  jd_variable = 5. We can even change the value of a variable by re-assigning it to a different value later.'],
                        ['Using the equal sign in Python', 'In the line 5 + 3 = 8, the equals sign means "is the same as".  In the line jd_variable = 5, the equals sign means "takes the value of".'],
                        ['Benefits of using variables', 'Variables can be useful to programmers in many ways:  They improve code readability by using names that make sense to humans. They give us a way to store the value of important data.  They give us a way to change the value of something (like in the line days = days-1).'],
                        ['Numbers versus Strings', 'In Python, 5 is a number while "5" is a string.  The code 5 + 5 would give 10.  The code "5" + "5" would give "55".'],
                        ['Functions', 'A function is something that takes input, does something to that input, and then produces output. For example, a function named sum3 might take 3 numbers as input and produce the sum of those numbers as output.'],
                        ['Making versus using a function', 'Functions are made by starting a line of code with the keyword <span class="code">def</span> and then giving a function name followed by the function parameters in parentheses. These parameters will eventually be replaced by actual values when the function is used (called).  In the "body" of the function, we write the code that specifies what to  do with the input parameters. For example the following code could be the definition of a function called sum3:  def sum3(a,b,c): / answer = a+b+c / return answer.  To use a function, we write the name of the function followed by the value(s) we want to give it in parentheses. Like this:  print sum3(1,2,3) >>>6'],
                        ['Functions help avoid repetition', 'Functions are tools that programmers can create and reuse forever! Once you\'ve defined a function once, you never have to define it again.'],
                        ['Not using the return statement', ' The return keyword tells Python exactly what the function should produce as output. If a function doesn\'t have a return statement, then you\'ll get behavior like this:  def add_ten(x): / answer = x + 10 / new_number = add_ten(7) / print new_number / >>>None'],
                        ['Comparisons to Make Decisions', 'Python uses comparisons to make decisons.  These expressions include:  equality to show copmarison (==), equal to show assignment (=), greater than or less than (> or <), not equal to show comparison (!=).'],
                        ['If function', 'If Statements control which code gets executed when. If statements are used to define procedures.  The test expression is evaluated and the Block will run if the test expression is true.  The block does not run if the test expression is false.  Statements inside the block are ran only if the test expression is true. The next statement that is not indented will be executed whether or not the test expression is true. If x<0 then x = -x'],
                        ['While Loops', 'While loops make code perfrom the same task many times. If statments perform 0 or 1 times where as While loops perform until the expression is False. '],
                        ['Break Statements', 'The break command allows you to get out of the While loop to move on to the next step.  is usedful when a loop goes on continuously and needs to stop.  You can add Break in an If statement within the While loop to makde sure the While loop does not go on for ever.'],
                        ['Structured Data', 'You can structure data using strings or list.  Strings is a sequence of characters identified with  \'jerry!\' where a List is a sequence of anything inside a bracket [0, 1, 2, 3, 4, 5]'],
                        ['Nested Lists', 'Nested Lists is a list of lists that can include strings and numbers.  Nested lists are used to help automated HTML coding.'],
                        ['Mutation', 'Mutation is being able to change the value of a list after it has been created. You can use the + sign to concatenate a strings.  With lists, you can change a specific element in the list.'],
                        ['List Operations', 'Append is used to mutate a list. You can append a list inside our outside a procedure.  ex. p = [1, 2], q = [3, 4], p.append(q), p = [1, 2, [3, 4]].  + is used to concatenate a list. <span class="code">Ex. [0,1] + [2,3] -> [0,1,2,3].   Len is used to find the length of any object that is a collection of things (strings, lists). ex. len([0,1]) >>> 2'],
                        ['Loops on Lists', 'For loops assign elements to a name and go through the block.  For loops are used when defining procedures. Examples were used to sum up a list and multiple a list of elements by each other.  While loops perform the same task until the expression is False.'] ]
                        

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print (make_HTML_for_many_concepts(JD_LIST_OF_CONCEPTS))