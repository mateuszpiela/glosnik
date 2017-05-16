function descriptor()
   return {
      title = "Tytul muzyki na port COM";
      version = "0.3";
      author = "";
      url = '';
      shortdesc = "Wlacz Tytul muzyki na porcie COM";
      description = "<div><b>Uwaga prototypowa wersja tylko pod linuxa !</b></div>";
      capabilities = { "input-listener" }
   }
end


function activate()
   vlc.msg.dbg("[VLC COM] ZALADOWANO POPRAWNIE ")
end

function input_changed()
    local item = vlc.input.item()
    local nazwa = item:name()
    local serial = io.open("/dev/ttyACM0","w")
    serial:write(nazwa)
    serial:flush()
end
