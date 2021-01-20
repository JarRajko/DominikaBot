Stručný popis:
Táto semestrálna práca je implementácia vlastného bota pre aplikáciu discord s použitím knižnice discord.py, ktorá nám dovoľuje manipulovať s rozhraním aplikácie pre discord ako klient (umožnuje posielať správy, upravovať správy, posielať embeds, meniť status, tagovať užívateľov atď.) 

Originalita:
Existuje veľa druhov botov pre discord, každý zameraný na niečo iné. Napríklad existuje veľa botov určených pre zábavu, zamerané iba na hry alebo vtipy a vtipné obrázky alebo boti určený iba na uľahčenie správy serveru bližší zoznam tu :  https://top.gg/list/top  . Náš Dominika bot je určený sčasti pre zábavu a sčasti ako nástroj. 

Použité knižnice (externé): 
Discord.py
Asyncio
restrictedPython
PyDictionary

Vysvetlivky:
Discord 
- Americká VoIP digitálna platforma pre vytváranie komunít pre okamžité zasielanie správ 

Bot 
- Skrátene od slova Robot, program určený na automatizáciu a zjednodušenie alebo pomoc s určitými úlohami

Server 
- Discord umožnuje si vytvoriť vlastný server na ktorý sa ostatní užívatelia môžu pripojiť a na serveri môžu užívatelia využívať textové „channel-y“ alebo „voice room“ a zdieľať obsah

Channel
- je kanál do ktorého môžu užívatelia posielať obrázky, súbory a textové správy 

Voice room (vr) 
- je hlasový kanál do ktorého sa užívateľ môže pripojiť a komunikovať s ostatnými užívateľmi

Embed správy 
- správa, ktorá sa kompozíciou podobá na webovú stránku, t.j môže mať header, footer a sekcie s obrázkami, je to štylizovaná správa

Rola 
- Role na discord serveri umožňujú spravovanie prístupu pre užívateľov, môžu zamedziť prístup užívateľom do channel-ov alebo voice room-iek alebo prideliť právomoci na spravovanie určitého obsahu
(napr mazať správy alebo vyhodiť užívateľa zo serveru)

Cogs 
- V knižnici discord.py sú takzvané cog-y ktoré sú navrhnuté pre rozdelenie súborov pri práci s touto knižnicou (niečo ako class-y)

Tagy 
- Discord.py knižnica využíva takzvané tagy, ktoré určujú povahu vytváraných metód
napr. tag  @command() sa používa pre vytváranie metód, ktoré sa spustia príkazom

Bot token 
- tajný token, ktorý spojí skript s aplikáciu

Avatar 
- zmenšená profilová fotka užívateľa

Prefix 
- text, ktorý sa používa pre aktivovanie bota

DM 
- skratka Direct message, správa priamo užívateľovi

Ban 
- zablokovanie a vyhodenie užívateľa zo serveru 

Dostupné príkazy:
    Dominika? antonymum cold >>> Zobrazí antonymum pre slovo cold (English only)
    Dominika? synonymum warm >>> Zobrazí synonymum pre slovo warm (English only)
    Dominika? meaning inappropriate >>> Zobrazí význam slova inappropriate (English only)
    Dominika? datum >>> Zobrazí aktuálny dátum, názov dňa, dnešné a zajtrajšie meniny ako embed
    Dominika? meniny Peter >>> Zobrazí dátum kedy má Peter meniny v slovenskom kalendári
    Dominika? meniny 22.2 >>> Zobrazí meno, kto má meniny v slovenskom kalendári 22. februára
    Dominika? meniny Petr cz >>> Zobrazí dátum, kedy má meniny Petr v českom kalendári
    Dominika? meniny 22.2 cz >>> Zobrazí meno, ktoré má meniny 22. februára v českom kalendári
    Dominika? pomoc prikazy >>> Zobrazí help ako embed pre všetky dostupné príkazy
    Dominika? pomoc *názov príkazu* >>> Zobrazí pomoc pre príkaz
    Dominika? ping >>> Zobrazí odozvu bota
    Dominika? run ```
    print("hello world")
    ``` >>> Zadaný python kód sa preloží a výstup sa vypíše (príkaz je značne obmedzený kvôli bezpečnosti)
    Dominika? zvelic Sample text >>> Odošle text s náhode kapitalizovanými písmenami
    Dominika? poke @user >>> Odošle DM adresátovi o tom, že ho zadávateľ príkazu štuchol
    Dominika? zmaz 5 >>> Zmaže 5 správ v roomke v ktorej sa príkaz vyvolal
    Dominika? tell "Text v úvodzovkách" @user >>> Odošle DM adresátovi so zadaným textom
    Dominika? say text >>> Odošle text do roomky v ktorej sa príkaz spustí a príkaz sa zmaže
    Dominika? diceroll >>> Hod kockou s animáciou
    Dominika? ban @user >>> Napíše správu, že uźívateľ dostal ban (ale ban nedostane)
    Dominika? Povedz, vyhrám v športke? >>> Odpovie na áno / nie otázky
    Dominika? ocen @user "Titul" "Popis" <URL obrázku> >>> Vytvorí embed so zadanými parametrami ako ocenenie
    /emoty >>> Odošle zoznam dostupných ascii emojis užívateľovi do správy
    



