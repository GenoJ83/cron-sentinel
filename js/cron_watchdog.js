function isOverdue(lastSeenSec, intervalSec, gracePeriodSec = 300, nowSec = null) {
  const now = nowSec || Math.floor(Date.now() / 1000);
  const elapsed = now - lastSeenSec;
  return elapsed > (intervalSec + gracePeriodSec);
}
module.exports = { isOverdue };
