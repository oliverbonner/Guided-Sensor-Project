<?php
/**
 *      This page is meant to output the Stock Price of Google in real-time data format. 
 *      The data will be picked by FusionWidgets XT real-time line chart and plotted on chart.
 *      You need to make sure that the output data doesn't contain any HTML tags or carriage returns.
 *      For the sake of demo, we'll just be generating a random value between 30 and 35 and returning the same.
 *      
 *      In real life applications, you can get the data from web-service or your own data systems, convert it into real-time data format and then return to the chart. 
 *
 */
          
//Read in data file
$pulsedata = fopen("pulse.txt", "r");		  
//$tempdata = escapeshellarg("tempdata.txt");		  
//$tempdata = escapeshellarg("temperature.txt");

//move to penultimate line
//fseek($tempdata, 2);

//Read in first line of file
$line = fgets($pulsedata);
//$line = `tail -n 1 $tempdata`; 
//print $line;
//split line at the comma
$pulseValue = strtok($line, ",");
$dateTimeLabel = strtok(",");

//close file
//fclose($tempdata);

//Generate a random value between 30 and 35
//$temperatureValue =rand(30,35);

//Get label for the data - time in format hh:mn:ss
//$dateTimeLabel = date('h:i:s'); 

//Now write it to output stream
print "&label=" . $dateTimeLabel . "&value=" . $pulseValue;?>
