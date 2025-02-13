function areYouPlayingBanjo(name) {
  return name + (name[0].toLowerCase() == 'r' ? ' plays' : ' does not play') + " banjo";
}





function areYouPlayingBanjo(name) {
  return name + (/^r/i.test(name) ? " plays " : " does not play ") + "banjo";
}




function areYouPlayingBanjo(name) {
  return name.toLowerCase().startsWith('r') ? name + " plays banjo" : name + " does not play banjo"
}