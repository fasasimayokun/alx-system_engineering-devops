#!/usr/bin/env ruby
# a ruby script that outputs: [SENDER],[RECEIVER],[FLAGS] phone number

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
