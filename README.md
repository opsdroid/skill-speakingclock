# opsdroid skill speakingclock

A skill for [opsdroid](https://github.com/opsdroid/opsdroid) to tell you the time every hour.

## Requirements

[pytz](http://pytz.sourceforge.net/)

## Configuration


```
skills:
  speakingclock:
    timezone: "America/Chicago"  # Optional local timezone
                                 # If not set will use opdroid.config.timezone if set,
                                 # otherwise UTC
    show_utc: false              # Optional, show UTC time with local
```

## Usage

This skill will trigger automatically every hour.

> "The time is now 18:00 [CST]"

You can also ask directly.

#### `what time is it?`

> "it is 10:02 [CST]"
