"""VDSC Rong Viet utils."""

# Request headers for the VDSC Rong Viet API

# NOTE: Visit https://livedragon.vdsc.com.vn/all/all.rv
# Open Developer Tools > Navigate to Network > Choose Fetch/XHR > Select any request > Find Cookie in Header > Copy value.
rv_cookie = "rv_cspm=1234; rv_avraaaaaaaaaaaaaaaa_session_=JIDBPDEDGIFIAHDFMACGGGINMFBDCDBOHCFGJPCDNBAJBMBMCDIJKIPAOGEGAMMNMKODNCIDEEHOPJKJDPKAGFBDMINKFPAOBGCLGEODFONGKOBELDCFMBFLHJBHGNNB; vdsc-liv=!bXg2YA6Or/B47j4SXRmvUcbihKKaHUemqvADkR1J8s3vcbherxHWgcMHtlEvblLDqUgw5Kh6LjOjWQ==; allCustomGroupsCkName=ALL_DEFAULT_GROUP_ID%23%23%23%23%23%23%23%23CTD%3BDHG%3BDRC%3BFPT%3BHPG%3BHSG%3BKDC%3BMWG%3BNT2%3BPAC%3BPC1%3BPNJ%3BTAC%3BVCB%3BVDS%3BVGC%3BVJC%3BVNM%3B%23%23%23%23%23%23%23%23T%C3%B9y%20ch%E1%BB%8Dn; isLoadAdvertise=TRUE; hideMarketChartCKName=0; RV08835624=080035c91e23c9751e012d42a9530a91e5386a1a09cf58737d1ed7985c2af19d5f4eb725285bbb7ea90c488902a512e29b24270452; lhc_per_={%22vid%22:%22aa8060086a9227589df9%22}; JSESSIONID=A3E022329D0BFAD7BD561C50B650CCBD; rv_avraaaaaaaaaaaaaaaa_session_=HKNIHIBJIGJAGJDNCLCHNNEDEBJHCOPOIGJFGJFEEHBOBAKBJBIKNKPGBNCGIEGDPMKDEMNNBEGMIHNNBCNAPFODMIBPECDGHPNNIDBMKCLMDFDGLAKILKPMHBDPFKDD; RV9cd20160034=08557ab163ab2000af50fe1912a59b1c3f0b72a227d1a6501ce953112bbc52eeb1a694e8351e6e5108dddf0c8f113000c4a2fbae1176123f2724fd14f7239b95905d6ccd2807057b2ed45072ddab8e932fb07a5768ab941916d77e0ad7fbbc67"

rv_headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "DNT": "1",
    "Origin": "https://livedragon.vdsc.com.vn",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0",
    "X-Requested-With": "XMLHttpRequest",
    "sec-ch-ua": '"Edge";v="114", "Chromium";v="114", "Not=A?Brand";v="24"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

rv_headers["Cookie"] = rv_cookie
