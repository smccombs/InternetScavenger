<?php
	/*
		IP2LOCATION DB11.LITE (free) - This dataset is used to locate physical locations of IP addresses. Updates are done once a year.
		http://lite.ip2location.com/database-ip-country-region-city-latitude-longitude-zipcode-timezone
		
		Dreamhost does not allow bash mysql file imports "LOAD DATA LOCAL INFILE 'IP2LOCATION-LITE-DB11.CSV'". Because their mysql databases are not on the same server as the shared hosting. Meaning your files are on another server and can't be accessed.

		A solution is to take the CSV, and converted it to a .sql file.
		
		Step 1:
			Open PhpmyAdmin and enter the database your using. Open sql and paste this to create your table.
				CREATE TABLE `ip2location_db11`(
					`ip_from` INT(10) UNSIGNED,
					`ip_to` INT(10) UNSIGNED,
					`country_code` CHAR(2),
					`country_name` VARCHAR(64),
					`region_name` VARCHAR(128),
					`city_name` VARCHAR(128),
					`latitude` DOUBLE,
					`longitude` DOUBLE,
					`zip_code` VARCHAR(30),
					`time_zone` VARCHAR(8),
					INDEX `idx_ip_from` (`ip_from`),
					INDEX `idx_ip_to` (`ip_to`),
					INDEX `idx_ip_from_to` (`ip_from`, `ip_to`)
				)
				
		Step 2:
			FTP the zip file to host (I tried uploading the csv but it failed.)
			Once the transfer completes SSH to the server and use this command to unzip the files.
				unzip IP2LOCATION-LITE-DB11.CSV.ZIP
		
		Step 3:
			Edit this .php file to add the correct mysql database info, file path, etc.
			Once complete FTP this file to your host and execute it by opening this file in a URL.
				http://search.shawnmccombs.com/IP2LOCATION-LITE-DB11.php
				
			It will display how many records are in the csv once converted.
		
		Step:
			This file will next auto execute a the new .sql file and start inserting all the new records.
			Open PhpmyAdmin again and check to make sure they all are uploaded.
			It took about 30mins for mine to finish (3,815,766 records.)
			During this step my chrome browers kept asking me to wait or reset. I hit wait three times then the page crashed.
			Use Bash command TOP to see if mysql CPU load is still high and keep checking the record count form phpmyadmin it should keep going up.
			
		Congratulations! You're done!
	*/

	// EDIT Database info - This starts the .sql file
	$host="xxx.shawnmccombs.com";
	$username="xxxxxxxxzzzxxxxz";
	$password="xxxxxxxxzzzxxxxx";
	$db_name="xxxxxxxxxxxzzzzzz";

	// EDIT PATH - This is used to read and write the new converted sql file.
	$csvfile = fopen("/home/shawnmcc/search.shawnmccombs.com/IP2LOCATION-LITE-DB11.CSV","r");
	$sqlfile = fopen("/home/shawnmcc/search.shawnmccombs.com/IP2LOCATION-LITE-DB11.sql", "w");
	
	$Counter = 0;
	
	while(! feof($csvfile)) {
		$Counter++;
		
		$sql = "INSERT INTO ip2location_db11 (ip_from, ip_to, country_code, country_name, region_name, city_name, latitude, longitude, zip_code, time_zone) VALUES(".fgets($csvfile).");\n";
		
		fwrite($sqlfile, $sql);
	}

	fclose($sqlfile);
	fclose($csvfile);
	
	echo "Done converting ".$Counter." lines!";
	
	// EDIT PATH - This starts the .sql file
	$output = shell_exec("mysql -u".$username." -p".$password." -h".$host." -D".$db_name." < /home/shawnmcc/search.shawnmccombs.com/IP2LOCATION-LITE-DB11.sql");
	
	echo "Done Inserting!";
?>