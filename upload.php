<?php

$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
if(isset($_POST["submit"])) {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {

        $old_path = getcwd();
        chdir('/var/www/html/resume_script');
        $output = exec('python3.6 main.py -f "/var/www/html/'.$target_file.'"');
        chdir($old_path);
        print_r($output);

    } else {
        print_r($_FILES);
        echo "Sorry, there was an error uploading your file.";
    }


}

?>