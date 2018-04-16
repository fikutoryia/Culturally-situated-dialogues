<?php
if($_POST['helpMe']) {
    
     if(!empty($_POST['mentalState'])){
        // Loop to store and display values of individual checked checkbox.
        foreach($_POST['mentalState'] as $mentalState)
        
        ($mentalState1=trim($mentalState . '/' . $mentalState1));
    }
    else{
        $mentalState1="no information";
    }
    
    $txt_file    = file_get_contents('out.txt');
    $txt_file=trim(str_replace(['\'', '{', '}'], '', $txt_file));
    $rows        = explode(",", $txt_file);
    //array_shift($rows);
    //foreach($rows as $row => $data)
    //echo $data . '---';
    $found=0;
    
    
    
echo "<html>
    <head>
       <link rel='stylesheet' type='text/css' href='design.css'>
        <title>Sample Web Form</title>
    </head>
    <body id=replybody>
    <div id=\"reply1\">";
    
foreach($rows as $row => $data)
{
    //echo $data . '---';
    $row_data = explode(':', $data);
    $info[$row]['state']          = $row_data[0];
    $state=trim($info[$row]['state']);
    //$state=trim(str_replace(['\'', '{', '}'], '', $info[$row]['state']));
    //echo $state;
    $info[$row]['action']         = $row_data[1];
    $action=trim($info[$row]['action']);
    //$action=trim(str_replace(['\'', '{', '}'], '', $info[$row]['action']));
   
    if (strcmp($action,"conceptIdentif")==0){
        $action="Identify the associated concept";
    }
    

      if (strcmp($action,"cultureIdentif")==0)
    {
        $action="Identify the user's culture";
    }

    //echo ($state . " - " . $mentalState1);
    if(strcmp($state,$mentalState1)==0) {
        echo $action;
        
        $found = 1;
        break;
    } 
    //echo '<br/>-end iteration-<br/><br/>';
}

if ($found==0) {
    
    echo "No action found. You can be creative!";
    
}

   
}
    
echo "</div></body></html>";