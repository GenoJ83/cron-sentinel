const { isOverdue } = require('../../js/cron_watchdog');

describe('Cron Watchdog', () => {
  it('returns true when elapsed time exceeds interval and grace period', () => {
    const now = 2000;
    const lastSeen = 1000; // 1000s ago
    const interval = 500;
    const grace = 100;
    expect(isOverdue(lastSeen, interval, grace, now)).toBe(true);
  });
  it('returns false when job is within grace period', () => {
    const now = 1050;
    const lastSeen = 1000;
    const interval = 100;
    const grace = 100;
    expect(isOverdue(lastSeen, interval, grace, now)).toBe(false);
  });
});
