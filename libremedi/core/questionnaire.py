# in darm 2 ho fatto in modo che si possa usare l'apostrofo (codice 18-21)

import glob
from random import choice

imgRnd = ("\n"
          "https://tuocoach.files.wordpress.com/2018/11/cambiamento-10.jpg?w=345&h=294\n"
          "https://organizzazioneaziendale.net/wp-content/uploads/2012/04/Pianificazione-e-Controllo-della-Produzione1.jpg\n"
          "https://image.freepik.com/free-vector/time-management-planning-events-flat-vector-illustration-design-business-concept-date-planning-organizing-events-events-management-icon-design_1223-140.jpg\n"
          "https://www.abparma.it/documenti/immagini/elaborati_pianificazione.jpg\n"
          "https://www.accademia.bcc.it/fusione/img/04-pianificazione-commerciale.png\n"
          "https://help.sap.com/doc/saphelp_byd1805_it/2018.05/it-IT/KTP/Software-Components/01200615320100003379/WEKTRA_for_Work_Centers/SCM/Ess/BillOfOperations/BOO_Structure1.png\n"
          "https://qsfera.it/media/k2/items/cache/1698b847c2e4fe98c05adcdc9d420590_XL.jpg\n").splitlines()


def createfile(filename, content):
    "Create a file"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        os.system(filename)
    except:
        print(
            "You must use an argument for the filename ('prova.html') and another for the content ('<b>Hello</b> World')")


def makeQ(q, ch):
    ch_html = "["
    for r in ch:
        ch_html += "\"" + r + "\","
    ch_html += "]"

    html = f"""{{
	        "question"      :   "{q}",
	        "image"         :   "{choice(imgRnd)}",
	        "choices"       :   {ch},
	        "correct"       :   "{ch[0]}",
	        "explanation"   :   "",
	    }},"""
    return html


qdic = {}


def mklist(filename):
    "Return a dictionary and a list of questions and aswers in a txt file where there is a question and answers for each line separated by an empty line for every group of question and answers"
    global qdic
    flist = []
    with open(filename, 'r', encoding='utf-8') as file:
        file = file.read()
        file = file.split("\n\n")
    for eachstring in file:
        flist.append(eachstring.split("\n"))
    for eachsublist in flist:
        for e in eachsublist:

            # avoid empty lines at the end
            if e == '':
                eachsublist.pop(eachsublist.index(e))
        # avoid empty lines at the end

        question = eachsublist[0]
        eachsublist.pop(0)
        qdic[question] = eachsublist
    return qdic


def menu():
    "a menu to choose a file in the directory 'data'"
    print("Test Files Below in Storage: data")
    print("------------------------------------")
    for number, eachfile in enumerate(glob.glob("data/file/*.txt")):
        print(number, eachfile.replace("data\\", ""))
    print("------------------------------------")
    file_number = int(input('Select the number of file? > '))
    fn = glob.glob("data/*.txt")[file_number]
    mklist(fn)


# print(mklist(fn))

htmlpage = ("\n"
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head>\n"
            "	<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n"
            "    <meta http-equiv=\"content-type\" content=\"text/html; charset=utf-8\">\n"
            "	<meta name=\"viewport\" content=\"initial-scale=1.0\">\n"
            "    <title>Quiz</title>\n"
            "    <!-- jquery for maximum compatibility -->\n"
            "	<link type=\"text/css\" rel=\"stylesheet\" href=\"https://stackpath.bootstrapcdn.com/twitter-bootstrap/2.2.1/css/bootstrap-combined.min.css\">\n"
            "    <!--<script src=\"http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js\"></script>-->\n"
            "	<script src=\"https://code.jquery.com/jquery-1.11.1.min.js\" integrity=\"sha256-VAvG3sHdS5LqTT+5A/aeq/bZGa/Uj04xKxY8KM/w9EE=\" crossorigin=\"anonymous\"></script>\n"
            "	<script src=\"https://stackpath.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js\"></script>\n"
            "    <script>\n"
            "\n"
            "    var quiztitle = \"Pianificazione e programmazione\";\n"
            "\n"
            "    /**\n"
            "    * Set the information about your questions here. The correct answer string needs to match\n"
            "    * the correct choice exactly, as it does string matching. (case sensitive)\n"
            "    *\n"
            "    */\n"
            "\n"
            "/**\n"
            "*Let's create the randomization of the questions!\n"
            "*/\n"
            "function speak(x) {\n"
            "  speechSynthesis.speak(new SpeechSynthesisUtterance(x));\n"
            "}\n"
            "function shuffle(array) {\n"
            "  var currentIndex = array.length, temporaryValue, randomIndex;\n"
            "\n"
            "  // While there remain elements to shuffle...\n"
            "  while (0 !== currentIndex) {\n"
            "\n"
            "    // Pick a remaining element...\n"
            "    randomIndex = Math.floor(Math.random() * currentIndex);\n"
            "    currentIndex -= 1;\n"
            "\n"
            "    // And swap it with the current element.\n"
            "    temporaryValue = array[currentIndex];\n"
            "    array[currentIndex] = array[randomIndex];\n"
            "    array[randomIndex] = temporaryValue;\n"
            "  }\n"
            "\n"
            "  return array;\n"
            "}\n"
            "\n"
            "if (!(\"scramble\" in Array.prototype)) {\n"
            "  Object.defineProperty(Array.prototype, \"scramble\", {\n"
            "    enumerable: false,\n"
            "    value: function() {\n"
            "      var o, i, ln = this.length;\n"
            "      while (ln--) {\n"
            "        i = Math.random() * (ln + 1) | 0;\n"
            "        o = this[ln];\n"
            "        this[ln] = this[i];\n"
            "        this[i] = o;\n"
            "      }\n"
            "      return this;\n"
            "    }\n"
            "  });\n"
            "}		\n"
            "\n"
            "let quiz = [\n")

endpage = """
];

//use this for IE syntax error at => : ECMA script 6 not supported in IE 11 :(
//quiz.forEach(function(q){ return q.choices.scramble()});

//use this for ECMA script 6
quiz.forEach(q => q.choices.scramble()); // Mescola l'ordine delle risposte
//console.log(quiz[0].choices);

quiz = shuffle(quiz); // mescola l'ordine delle domande

    /******* No need to edit below this line *********/
    var currentquestion = 0, score = 0, submt=true, picked;

    jQuery(document).ready(function($){

        /**
         * HTML Encoding function for alt tags and attributes to prevent messy
         * data appearing inside tag attributes.
         */
        function htmlEncode(value){
          return $(document.createElement('div')).text(value).html();
        }

        /**
         * This will add the individual choices for each question to the ul#choice-block
         *
         * @param choices array The choices from each question
         */
		function addChoices(choices){
			if(typeof choices !== "undefined" && $.type(choices) == "array"){
				$('#choice-block').empty();
				for(var i=0;i<choices.length; i++){
          // added .css({'font-size':'36px'}) il 2 marzo 2019
				$(document.createElement('li')).addClass('choice choice-box btn').attr('data-index', i).text(choices[i]).appendTo('#choice-block').css({'font-size':'28px'});		//  Aggiunge risposte
        }
			}
		}

        /**
         * Resets all of the fields to prepare for VAI ALLA PROSSIMA DOMANDA
         */
		function nextQuestion(){
			submt = true;
			$('#explanation').empty();
			$('#question').text(quiz[currentquestion]['question']);
			$('#pager').text('Domanda' + Number(currentquestion + 1) + ' di ' + quiz.length);
			if(quiz[currentquestion].hasOwnProperty('image') && quiz[currentquestion]['image'] != ""){
				if($('#question-image').length == 0){
					$(document.createElement('img')).addClass('question-image').attr('id', 'question-image').attr('src', quiz[currentquestion]['image']).attr('alt', htmlEncode(quiz[currentquestion]['question'])).insertAfter('#question');
				} else {
					$('#question-image').attr('src', quiz[currentquestion]['image']).attr('alt', htmlEncode(quiz[currentquestion]['question']));
				}
			} else {
				$('#question-image').remove();
			}
			addChoices(quiz[currentquestion]['choices']);
			setupButtons();

			jQuery(document).ready(function($){
				$("#question").html(function(){
					var text= $(this).text().trim().split(" ");
					var first = text.shift();
					return (text.length > 0 ? "<span class='number'>"+ first +"</span> " : first) + text.join(" ");
				});

				$('p.pager').each(function(){
					var text = $(this).text().split(' ');
					if(text.length < 2)
						return;

					text[1] = '<span class="qnumber">'+text[1]+'</span>';
					$(this).html(
						text.join(' ')
					);
				});

			});

        }

        /**
         * After a selection is submitted, checks if its the right answer
         *
         * @param choice number The li zero-based index of the choice picked
         */
        function processQuestion(choice){
          // Risposta ESATTA!
            if(quiz[currentquestion]['choices'][choice] == quiz[currentquestion]['correct']){
				$('.choice').eq(choice).addClass('btn-success').css({'font-size':'36px', 'font-weight':'bold', 'border-color':'#51a351', 'color':'#fff'});
				$('#explanation').html('<span class="correct">ESATTO!</span> ' + htmlEncode(quiz[currentquestion]['explanation']));
				score++;
              speak("esatto!");
              //nextQuestion();
			} else {
                $('.choice').eq(choice).addClass('btn-danger').css({'font-weight':'bold', 'border-color':'#f93939', 'color':'#fff'});
                $('#explanation').html('<span class="incorrect">INESATTO!</span> ' + htmlEncode(quiz[currentquestion]['explanation']));
        speak("Non è corretto! La risposta era " + quiz[currentquestion]['correct']);
            }
            currentquestion++;

			if(currentquestion == quiz.length){ // SONO FINITE LE DOMANDE... MOSTRA I RISULTATI
				$('#submitbutton').html('GET QUIZ RESULTS').removeClass('btn-success').addClass('btn-info').css({'border-color':'#3a87ad', 'color':'#fff'}).on('click', function(){
					$(this).text('GET QUIZ RESULTS').on('click');
					endQuiz();
				})

			} else if (currentquestion < quiz.length){ // SE CI SONO ANCORA DOMANDE, RIMETTE IL PULSANTE CONTROLLA LA RISPOSTA
				$('#submitbutton').html('VAI ALLA PROSSIMA DOMANDA &raquo;').removeClass('btn-success').addClass('btn-warning').css({'font-weight':'bold', 'border-color':'#faa732', 'color':'#fff'}).on('click', function(){
					$(this).text(' CONTROLLA LA RISPOSTA ').removeClass('btn-warning').addClass('btn-success').css({'font-weight':'bold', 'border-color':'#51a351', 'color':'#fff'}).on('click');
					nextQuestion(); // VA ALLA PROSSIMA DOMANDA
				})
			} else {
				//	$('#submitbutton').html('VAI ALLA PROSSIMA DOMANDA &raquo;').on('click', function(){
				//		$(this).text('- CONTROLLA LA RISPOSTA -').css({'color':'inherit'}).on('click');
				//	})
			}

          speak(quiz[currentquestion]['question'])

		}

        /**
         * Sets up the event listeners for each button.
         */
		function setupButtons(){

			$('.choice').on('click', function(){
				picked = $(this).attr('data-index');
				$('.choice').removeAttr('style').off('mouseout mouseover');
				$(this).css({'font-weight':'900', 'border-color':'#51a351', 'color':'#51a351', 'background' : 'gold'});
				if(submt){
					submt=false;
					$('#submitbutton').css({'color':'#fff','cursor':'pointer'}).on('click', function(){
						$('.choice').off('click');
						$(this).off('click');
						processQuestion(picked);
					});
				}
			})
		}

        /**
         * Quiz ends, display a message.
         */
		function endQuiz(){
			$('#explanation').empty();
			$('#question').empty();
			$('#choice-block').empty();
			$('#submitbutton').remove();
			$('.rsform-block-submit').addClass('show');
			$('#question').text("You got " + score + " out of " + quiz.length + " correct.");
			$(document.createElement('h4')).addClass('score').text(Math.round(score/quiz.length * 100) + '%').insertAfter('#question');			
		}

        /**
         * Runs the first time and creates all of the elements for the quiz
         */
		function init(){
      speak(quiz[currentquestion]['question'])
			//add title
      /*
			if(typeof quiztitle !== "undefined" && $.type(quiztitle) === "string"){
				$(document.createElement('h2')).text(quiztitle).appendTo('#frame');
			} else {
				$(document.createElement('h2')).text("Quiz").appendTo('#frame');
			}
      I removed the title to leave more space */

			//add pager and questions
			if(typeof quiz !== "undefined" && $.type(quiz) === "array"){
				//add pager

				$(document.createElement('p')).addClass('pager').attr('id','pager').text('Domanda 1 di ' + quiz.length).appendTo('#frame');
				//add first question
				$(document.createElement('h3')).addClass('question').attr('id', 'question').text(quiz[0]['question']).appendTo('#frame');
				//add image if present
				if(quiz[0].hasOwnProperty('image') && quiz[0]['image'] != ""){
					$(document.createElement('img')).addClass('question-image').attr('width','100px').attr('id', 'question-image').attr('src', quiz[0]['image']).attr('alt', htmlEncode(quiz[0]['question'])).appendTo('#frame');
				}

				$(document.createElement('p')).addClass('explanation').attr('id','explanation').html('').appendTo('#question');

				//questions holder
				$(document.createElement('ul')).attr('id', 'choice-block').appendTo('#frame');

				//add choices
				addChoices(quiz[0]['choices']);

				//add submit button
				$(document.createElement('div')).addClass('btn-success choice-box').attr('id', 'submitbutton').text('- CONTROLLA LA RISPOSTA -').css({'font-weight':'bold', 'color':'#fff','padding':'30px 0', 'border-radius':'10px'}).appendTo('#frame');

				setupButtons();
			}
		}

		init();

	});

	jQuery(document).ready(function($){			
		$("#question").html(function(){
		var text= $(this).text().trim().split(" ");
		var first = text.shift();
			return (text.length > 0 ? "<span class='number'>"+ first +"</span> " : first) + text.join(" ");
		});

		$('p.pager').each(function(){
			var text = $(this).text().split(' ');
			if(text.length < 2)
				return;

			text[1] = '<span class="qnumber">'+text[1]+'</span>';
			$(this).html(
				text.join(' ')
			);
		});

	});	

		function copyText() {
			var output = document.getElementById("frame").innerHTML;
			document.getElementById("placecontent").value = output;
		}

    </script>
    <style type="text/css" media="all">

      .btn:hover, .btn:active {
        color: blue;
        font-weight: 800;
      background-image: url("http://www.myiconfinder.com/uploads/iconsets/65192ff2984e9928d32fd577bc743ea5.png");
        background-size: 100%;

      }

      /*        BODY                 */
body {
    margin: 0;
    font-family: "Consolas",Helvetica,Arial,sans-serif;
    font-size: 24px;
    line-height: 20px;
    color: #ffffff;
    background-color: #21517ee8;
}
    h3.question {
    font-family: "Consolas",Helvetica,Arial,sans-serif;
    font-weight: normal;
    margin: 20px 0;
    padding: 0;
    font-style: italic;
    display: block;
    color: whitesmoke;

}  

		input 	

      { height:30px !important; }

		input[type=checkbox]

      { height:30px !important; margin-top:-3px !important; 
        margin-right:5px !important; box-shadow:none; background-color:#ffffff;
        position:relative !important; }

		textarea												
      { width: 90%; margin: 0 auto; display: block; }

		input[type=radio]								
      { height:30px !important; margin-top:-3px !important; margin-right:5px !important; box-shadow:none; background-color:#ffffff; position:relative !important; }

		.form-group input, .form-group select 					{ height:30px; padding: 0px 12px; }
		.form-horizontal .form-group							{ margin:10px; }
		.formContainer .formControlLabel 						{ width:auto !important; min-width:150px; margin:0; padding:0; }
		.formControls											{ width:100%; padding:0; margin: 10px 0 20px auto; }
		.radio 													{ padding-top:0 !important; padding-left:8px !important; }
		.radio-inline											{ margin-right:10px; padding-top:0 !important; display:inline; }
		.bold													{ font-weight:bold; }
		.italic 												{ font-style:italic; }
		.clear					 								{ width:100%; margin:0 !important; }
		.rsform-block-submit 									{ display:none; }
		.show 													{ display: block !important; }
		#submit													{ margin:0 auto; display:block; }

		/* QUIZ STYLES */
      li.choice-block {font-size: 28px};
		ol,ul 													{ list-style:none; font-size: 48}
		strong 													{ font-weight:700; }
		#frame 													{ width:auto; max-width: 800px; background:transparent; margin:3px auto; padding:10px;     color: #f94a4a !important; }
		div#frame h2 ul li											{ color: white; width:auto; border-bottom:1px solid #bdbdbd; padding:0 0 5px 0; font-size:32px; }
		h3.question 											{ font-weight:normal; margin:20px 0; padding:0; font-style:italic; display:block; }
		p.pager 												{ margin:5px 0 5px; color:#999; text-align:right; }
		.qnumber 												{ font-size:25px; font-weight:bold; font-style:italic; vertical-align:bottom; }
		.number 												{ font-family: "Consolas",Helvetica,Arial,sans-serif;font-size:24px; font-weight:bold; font-style:normal; vertical-align:inherit; padding-right:10px; }
		.score 													{ width:100%; display:inline-block; margin:30px 0; font-size:100px; text-align:center; }
		img.question-image 										{ width:25%; height:auto; display:block; max-width:150px; margin:10px auto; border:1px solid #ccc; }
		#choice-block 											{ display:block; list-style:none; margin:0; padding:0; cursor: pointer; }
	/*	#submitbutton 											{ cursor:pointer; -webkit-border-radius: 5px; -moz-border-radius: 5px; border-radius: 5px; } */
	/*	#submitbutton:hover 									{ background:#7b8da6; } */
		#explanation 											{ width:auto; min-height:0px; margin:0 auto; padding:0px 0; text-align:center;}
		#explanation span 										{ font-weight:bold; padding-right:8px; }
		.choice-box 											{ width:100%;  display:block;  text-align:center;  margin:5px auto !important; padding:10px 0 !important; border:1px solid #bdbdbd; }
      .choice-box.btn {font-size: 28px;}
		.correct 												{ color:#51a351; font-size: 32px; display: block; margin-bottom: 5px; border-bottom: 1px #51a351 solid; padding-bottom: 5px; }
		.incorrect 												{ color:#f93939; font-size: 32px; display: block; margin-bottom: 5px; border-bottom: 1px #f93939 solid; padding-bottom: 5px; }

#body{
width:100vw;
height:100vh;
}

    </style>

</head>
<!-------------------------------- [ AUDIO ] ----------------------------->
<audio id="soundtrack">  <source src="https://cdn.glitch.com/1e8a1dde-7ab4-43db-8ec8-1ccb6d3cad7f%2Fanswer_20sec.ogg?1551595183210"></audio>
<script>
var soundtrack = document.getElementById("soundtrack");
soundtrack.volume = 0.4;
window.onreload = soundtrack.play()
</script>
<!-------------------------------- [ AUDIO ] ----------------------------->

</script>
<body>
   <!--  glitch button for remix --------------------------------->
<script src="https://button.glitch.me/button.js"></script>
<div class="glitchButton" style="position:fixed;top:50px;right:20px;z-index:1;"></div>
  <div id='audio' style="position:fixed;top:100px;right:20px;z-index:1;"><a href="javascript:soundtrack.volume=0;">OFF</a></div>
    <div id='audio' style="position:fixed;top:100px;right:70px;z-index:1;"><a href="javascript:soundtrack.volume=0.5;">ON</a></div>
  <!-- home button -->
  <div id="menuDiv">
<script src="https://quarta.glitch.me/dropdownclassi.js"></script>
</div>




<div class="form-group rsform-block rsform-block-framecontent"><div id="frame" role="content"></div>

</div>
<script>


  </script>


</body>
</html>
"""


def createDarm():
    global htmlpage
    for d in qdic:
        htmlpage += makeQ(d, qdic[d])
    htmlpage += endpage
    createfile("paste_in_darm.html", htmlpage)


menu()
createDarm()
