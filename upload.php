<?php

$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
if(isset($_POST["submit"])) {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {

        $old_path = getcwd();
        chdir('/var/www/html/resume_script');
        $scriptPython = exec('python3.6 main.py -f "/var/www/html/'.$target_file.'"');
        $outputPython = file_get_contents('/var/www/html/resume_script/data.json');
        chdir('/var/www/html/ResumeParser/ResumeTransducer');
        $scriptJava = exec('java -cp "bin/*:../GATEFiles/lib/*:../GATEFiles/bin/gate.jar:lib/*" code4goal.antony.resumeparser.ResumeParserProgram "/var/www/html/'.$target_file.'" data.json');
        $outputJava = file_get_contents('/var/www/html/ResumeParser/ResumeTransducer/data.json');
        chdir($old_path);
        echo "JAVA";
        print_r($outputJava);
        echo "PYTHON";
        print_r($outputPython);

        $associativeFromPythonParser = json_decode($outputPython, true);
        $associativeFromJavaParser = json_decode($outputJava, true);
        $result = array_merge($associativeFromPythonParser, $associativeFromJavaParser);

        print_r($outputPython);

    } else {
        print_r($_FILES);
        echo "Sorry, there was an error uploading your file.";
    }
}

?>
