filename pype pipe 'python students.py';
data students;
	infile pype missover dsd firstobs=1;
	length student_school $50. student_sis_id $50. student_name_middle $50. student_name_last $50.
	       student_name_first $50. student_district $50. student_hispanic_ethnicity $50. student_dob $50.
	       student_gender $50. student_frl_status $50. student_iep_status $50. student_grade $50.
	       student_credentials_district_pwd $50. student_credentials_district_usr $50.
	       student_race $50. student_created $50. student_location_zip $50. student_last_modified $50.
	       student_student_number $50. student_id $50. student_state_id $50. student_ell_status $50.
	       student_email $50.;
    input student_school $ student_sis_id $ student_name_middle $ student_name_last $ student_name_first $
	      student_district $ student_hispanic_ethnicity $ student_dob $ student_gender $ student_frl_status $
	      student_iep_status $ student_grade $ student_credentials_district_pwd $
	      student_credentials_district_usr $ student_race $ student_created $ student_location_zip $
	      student_last_modified $ student_student_number $ student_id $ student_state_id $ student_ell_status $
          student_email $;
run;
