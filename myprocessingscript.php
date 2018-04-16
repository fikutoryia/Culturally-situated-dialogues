<?php

if($_POST['reinfButton']) {
        if(!empty($_POST['mentalState'])){
        // Loop to store and display values of individual checked checkbox.
        foreach($_POST['mentalState'] as $mentalState)
        ($mentalState1=$mentalState . '/' . $mentalState1);
        echo $mentalState1;
    }

        if(!empty($_POST['mentalState2'])){
        // Loop to store and display values of individual checked checkbox.
        foreach($_POST['mentalState2'] as $mentalState)
        ($mentalState2=$mentalState . '/' . $mentalState2);
    }


        if(isset($mentalState1) && isset($_POST['action']) && isset($mentalState2)) {
        $data = $mentalState1 . '-' . $_POST['action'] . '-' . $mentalState2 . "\n";
        $ret = file_put_contents('matrix.txt', $data, FILE_APPEND | LOCK_EX);
        if($ret === false) {
        die('There was an error writing this file');
    }
    
   
}
    
        $command = escapeshellcmd('python __init__.1.py');
        $output = shell_exec($command);
        echo $output;
}




if($_POST['nextObservation']){

if(!empty($_POST['mentalState'])){
// Loop to store and display values of individual checked checkbox.
foreach($_POST['mentalState'] as $mentalState)
($mentalState1=$mentalState . '/' . $mentalState1);

}
else{
    
    $mentalState1="no information";
}


if(!empty($_POST['mentalState2'])){
// Loop to store and display values of individual checked checkbox.
foreach($_POST['mentalState2'] as $mentalState)
($mentalState2=$mentalState . '/' . $mentalState2);
}

else{
    
    $mentalState2="no information";
}


if(isset($mentalState1) && isset($_POST['action']) && isset($mentalState2)) {
    $data = $mentalState1 . '-' . $_POST['action'] . '-' . $mentalState2 . "\n";
    $ret = file_put_contents('matrix.txt', $data, FILE_APPEND | LOCK_EX);
    if($ret === false) {
        die('There was an error writing this file');
    }
    
  else {
   header('Location: ' . $_SERVER['HTTP_REFERER']);
}
}
   
else {
   die('no post data to process');
}

}
