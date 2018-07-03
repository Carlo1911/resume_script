
<?php

$target_dir = "uploads/";
$target_file = $target_dir . basename($_FILES["fileToUpload"]["name"]);
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    if (move_uploaded_file($_FILES["fileToUpload"]["tmp_name"], $target_file)) {

        $old_path = getcwd();
        chdir('/var/www/html/resume_script');
        $output = exec('python3.6 main.py -f "test/Adrien CHOROT.docx"');
        chdir($old_path);
        print_r($output);
        print_r($target_file);
        echo "The file ". basename( $_FILES["fileToUpload"]["name"]). " has been uploaded.";
        
    } else {
        print_r($_FILES);
        echo "Sorry, there was an error uploading your file.";
    }

    
}

?>