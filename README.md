# watch-face-wearfit
 
 A collection of watch face binary files.
 
 ## Installation
 
 They can be installed using Chronos app
 
 <a href='https://play.google.com/store/apps/details?id=com.fbiego.chronos&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1'><img alt='Get it on Google Play' height="100px" src='https://play.google.com/intl/en_us/badges/static/images/badges/en_badge_web_generic.png'/></a>


> **Warning**
> Install faces at your own risk as they may not be compatible with your watch

## Tools

The [`extract.kt`](tools/extract.kt) file can be used to rebuild the watchface background for the purpose of viewing only. Modifying the background is not yet possible for use as a watch face.

Compile > `kotlinc extract.kt -include-runtime -d extract.jar`

Rebuild > `java -jar extract.jar 107_2_dial.bin 774 0`

The output can be viewed using [`rawpixels.net`](http://rawpixels.net/) using the following settings:

- `240` x `240`
- `RGB565` format
- Little Endian enabled

> **Note**
> experimental tool
