filename pype pipe 'python districts.py';
data districts;
    infile pype missover dsd firstobs=1;
    informat id $50. name $100.;
    input id $ name $;
run;
