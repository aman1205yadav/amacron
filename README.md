# amacron
Utility to conver english formatted crons to linux understandable cron

amacron: [TYPE] [INTERVAL_VALUE] [INTERVAL_SCOPE]

[INTERVAL_TYPE]
Function:   It defines the occurrence of intervals.
Values:     every|first|at
Details:    Amacron must start with any of these supported interval types.

[INTERVAL_UNIT]
Function:   It represents the unit of time.week can only be used with 'first'([TYPE]).
Values:     minute(s)|min(s)|hour(s)|day(s)|week(s)|month(s)
Details:    Amacron can be created by combining interval types with the given units.
            Except week' which can only be combined with 'first' interval type.

[INTERVAL_SCOPE]
Function:   It defines the scope during which the job will run.
Values:     from|from and to|at|hours|minutes|days|HH:MM (24H format)
Details:    The scope is a combination of one or two of the supported values.
            Time in HH:MM format is supported only with the 'from' and 'from and to' scope.
            Prefixes like 'st|nd|rd|th' can be used for hours/minutes/days.

Examples with descriptions:

every 5 hours                       'every' can be used to create generic interval cron
at 12th minute                      'at' can be used to specify specific time intervals
every 5 hours from 10:00 to 23:00   'from' and 'to' can be used to construct confined intervals
first of every 5 months             'first' can be used to specify intervals to begin at given scope
first of every week                 'first' can be combined with 'every' for special cases

Combinations like this can be created using amacron which returns its corresponding cron value.
