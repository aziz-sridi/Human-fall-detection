import csv

# Provided data
data = """1 11 874 1011 1
1012 1079 6
1080 1108 2
1109 1285 3
2 4 308 374 1
375 399 2
400 600 3
3 11 380 590 1
591 625 2
626 784 3
4 6 230 287 1
288 314 2
315 380 3
381 600 6
601 638 2
639 780 3
5 11 288 310 1
311 336 2
337 450 3
6 1 325 582 1
583 629 2
630 750 3
7 6 330 475 1
476 507 2
508 680 3
8 4 144 270 1
271 298 2
299 380 3
9 11 310 472 1
473 505 5
506 576 7
577 627 6
628 651 2
652 760 3
10 11 315 461 1
462 511 5
512 530 2
531 680 3
11 7 378 463 1
464 489 2
490 600 3
12 11 355 604 1
605 653 2
654 770 3
13 4 301 430 1
431 476 5
477 525 7
526 636 5
637 717 8
718 780 6
781 822 6
823 863 2
864 960 3
14 6 372 555 1
556 590 5
591 856 8
857 934 6
935 988 6
989 1023 2
1024 1115 3
15 11 363 486 1
487 530 5
531 630 7
631 754 6
755 787 2
788 870 3
16 4 380 455 1
456 488 5
489 530 4
531 568 6
569 629 5
630 645 4
646 670 6
671 731 5
732 817 7
818 890 6
891 940 2
941 1000 3
17 6 251 315 1
316 340 5
341 361 4
362 388 6
389 410 5
411 430 4
431 460 6
461 531 5
532 620 7
621 729 6
730 770 2
771 860 3
18 6 301 378 1
379 430 5
431 530 7
531 570 6
571 601 2
602 740 3
19 10 255 498 1
499 600 2
601 770 3
20 11 301 544 1
545 672 2
673 800 3
21 11 408 537 1
538 608 5
609 794 7
795 863 6
864 901 2
902 1040 3
22 1 317 586 1
587 685 5
686 737 7
738 766 6
767 808 2
809 930 3
23 11 393 662 1
663 688 5
689 710 4
711 744 6
745 1519 1
1520 1595 2
1596 1661 6
1662 1730 1
1731 1769 5
1770 1839 4
1840 1886 6
1887 2645 1
2646 2698 5
2699 2958 8
2959 3035 6
3036 3156 1
3157 3237 5
3238 3416 8
3417 3573 6
3574 3614 2
3615 3745 6
3746 3795 5
3796 4042 4
4043 4105 6
4106 4204 1
4205 4264 5
4265 4440 7
4441 4527 6
4528 5200 1
24 6 350 974 1
975 1315 1
1316 1351 5
1352 1414 4
1415 1450 6
1451 1750 1
1751 1805 5
1806 1844 4
1845 1884 6
1885 2490 1
2491 2514 5
2515 2563 4
2564 2587 6
2588 3040 1
3041 3077 5
3078 3125 6
3126 3243 1
3244 3353 1
3354 3401 5
3402 3500 4"""

# Split the data into lines
lines = data.split("\n")

# Create a CSV file and write the data
with open("fall_dataset.csv", "w", newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',')
    csv_writer.writerow(['Scenario', 'Camera Reference', 'Period Start', 'Period End', 'Position Code'])

    for line in lines:
        values = line.split()
        if values:
            csv_writer.writerow(values)
