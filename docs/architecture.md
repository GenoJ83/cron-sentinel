# Architecture

```mermaid
flowchart LR
    Cron[Cron Job Runner] --> Wrapper[Execution Wrapper]
    Wrapper --> Heartbeat[Dead Man Switch]
    Heartbeat --> Watchdog[Timeout Watchdog]
    Watchdog --> Alert[Discord / Slack Alert]
```
