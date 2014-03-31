filename pype pipe 'python schools.py';
data schools;
	infile pype missover dsd firstobs=1;
	length school_sis_id $50. school_name $50. school_district $50. school_school_number $50. school_created $50.
			school_nces_id $50. school_phone $50. school_high_grade $50. school_last_modified $50.
			school_location_city $50. school_location_state $50. school_location_zip $50. school_location_address $50.
			school_state_id $50. school_principal_name $50. school_principal_email $50. school_id $50.
			school_low_grade $50.;
	input school_sis_id $ school_name $ school_district $ school_school_number $ school_created $ school_nces_id
		$ school_phone $ school_high_grade $ school_last_modified $ school_location_city $ school_location_state
		$ school_location_zip $ school_location_address $ school_state_id $ school_principal_name
		$ school_principal_email $ school_id $ school_low_grade $;
run;
