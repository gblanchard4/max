max
===
Insert description here

# Phase one
Can only handle fastq/fastq.gz input at this point
```
| fastq
|
└─── Quality Filtering ───> RSEM ───> Human Quantification
			|
			|
			└─── STAR (RNA Default)
						|
						|
						└─── Aligned SAM
								|
							/─── ───\
				Mapped Reads		Unmapped Reads
```
			