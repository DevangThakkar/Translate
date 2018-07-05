PERL=/home/martink/bin/perl
TABLEVIEWER_DIR=/home/martink/work/circos/svn/tools/tableviewer
CIRCOS_DIR=/home/martink/work/circos/svn-tags/circos-tableviewer/
WORKING_DIR=/home/martink/www/htdocs/tableviewer/tmp/wscpxgf
cd /home/martink/www/htdocs/tableviewer/tmp/wscpxgf
$PERL $TABLEVIEWER_DIR/bin/parse-table -conf etc/parse-table.conf -file uploads/table.txt -segment_order=ascii,size_desc -placement_order=row,col -interpolate_type count -col_order_row -use_col_order_row -row_order_col -use_row_order_col -row_color_col -use_row_color_col -color_source row -transparency 1 -fade_transparency 0 -ribbon_layer_order=size_asc > data/parsed.txt
cat data/parsed.txt | $TABLEVIEWER_DIR/bin/make-conf -dir data
$PERL $CIRCOS_DIR/bin/circos -param random_string=wscpxgf -conf etc/circos.conf
cd /home/martink/www/htdocs/tableviewer/tmp/wscpxgf; /home/martink/bin/perl /home/martink/work/circos/svn-tags/circos-tableviewer//bin/circos -param random_string=wscpxgf -conf /home/martink/www/htdocs/tableviewer/tmp/wscpxgf/etc/circos.conf 2>&1 > /home/martink/www/htdocs/tableviewer/tmp/wscpxgf/results/report.txt
tar cvfz circos-tableviewer-wscpxgf.tar.gz *
