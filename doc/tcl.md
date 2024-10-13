# /opt/miniconda/bin/tclsh

puts "Hello World!"
set  marks(english) 80
#IMP: indices are under normal brackets
set myVariable {red green blue}
#IMP: List is under {}
## Bbox overlap

# Bounding Box 1
set x1 0
set y1 0
set width1 5
set height1 5

# Bounding Box 2
set x2 3
set y2 3
set width2 5
set height2 5

# Calculate the coordinates of the corners for each box
set x1_end [expr {$x1 + $width1}]
set y1_end [expr {$y1 + $height1}]

set x2_end [expr {$x2 + $width2}]
set y2_end [expr {$y2 + $height2}]

# Check for overlap
if {($x2_end >= $x1 && $x1_end >= $x2) && ($y2_end >= $y1 && $y1_end >= $y2)} {
    puts "The bounding boxes overlap!"
} else {
    puts "The bounding boxes do not overlap."
}

# Define a dictionary to represent a bounding box
set box1 [dict create]
dict set box1 x 0
dict set box1 y 0
dict set box1 width 5
dict set box1 height 5

# Accessing fields in the structure
set x1 [dict get $box1 x]
set y1 [dict get $box1 y]
set width1 [dict get $box1 width]
set height1 [dict get $box1 height]

# Print the values
puts "Box 1:"
puts "x: $x1"
puts "y: $y1"
puts "width: $width1"
puts "height: $height1"

# Arrays
array set myArray {
    key1 value1
    key2 value2
    key3 value3
}

# Alternatively, you can assign values individually:
set myArray(key4) value4


#Prompts
# Give me a brief tutorial on tcl
# How about arrays