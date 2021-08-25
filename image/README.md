## ImageMagick
resize images with:
```
convert frog.png -resize 64x64 frog_sm.png
```

convert to Netpbm graymap ascii (magic P2)
```
convert frog.png -compress none frog.pgm
```

convert to Netpbm graymap binary (magic P5)
```
convert frog.png frog.pgm
```

identify files with:
```
identify frog.png
identify -verbose frog.png
```

### remarks
- jpeg is interesting because it preserves the comments from the PGM file
