task();

sub task{
	for (my $i=0;$i <= 99999999999999999999; $i++){
		print "\n ---------------------------------------";
		my @j = (0...100);
		foreach my $a(@j){
			my $ans = $a*$i;
			print "\n $i * $a = $ans";
		}
		
	} 
	

}
