# Utility to close a bunch of common programs before booting up steam

to_close = [
  'Messages.app',
  'Chrome',
  'Spotify',
  'puma',
  'rails',
  'Sequel',
  'Code.app',
  'Notes.app',
  'Monitor.app',
  'iTerm.app'
]

greps = to_close.map { |tc| "-e #{tc} " }.join("")

pids = (`ps aux | grep #{greps} | grep -v grep | awk '{print $2}'`).split("\n")

pids.each do |pid|
  (`kill -9 #{pid}`)
end
