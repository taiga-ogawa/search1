#! /usr/local/bin/perl

$input = <STDIN>;
chop($input);

#@keyword = split(/ /,$input);
$keyword = $input;

$count = 0;
open(TARGET,"target.txt");
while($line = <TARGET>){
  if($line =~ /^#/){
    next;
  }
  if($line =~ /$keyword/i){
    chop($line);
    $match[$count] = $line;
    ++($count);
  }
}
close(TARGET);

if($count > 0){
  for($i = 0 ; $i < $count ; ++($i)){
    print "$match[$i]\n";
  }
}

#end



