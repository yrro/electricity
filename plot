set timefmt "%Y-%m-%d"
set xdata time
set format x "%Y-%m"
plot for [col=2:3] "data" using 1:col
pause mouse close

# vim: ft=gnuplot
