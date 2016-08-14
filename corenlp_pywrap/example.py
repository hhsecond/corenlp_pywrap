import pywrap as p
import logging
p.root.setLevel(logging.DEBUG)
cn = p.CoreNLP()
sent = ''' .cb-list-heading{font-weight:normal!important} MOBILE SITE & APPSm.cricbuzz.comAndroidiOSWindows MobileBlackberryChrome ExtensionFOLLOW US ONfacebooktwittergoogle+PinterestRSS FeedCOMPANYCareersAdvertisePrivacy PolicyTerms of UseCricbuzz TV Ads© 2016 Cricbuzz.com, Times Internet Limited. All rights reserved | The Times of India | Navbharat Timesvar script_tag = document.getElementsByTagName('script')[0];	(function() {	var cmin = document.createElement('script'); cmin.type = 'text/javascript'; cmin.async = true;	cmin.src = 'http://i.cricketcb.com/statics/site/js/cricbuzz.min.1466404921.js';	script_tag.parentNode.insertBefore(cmin, script_tag);	})();(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':	new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],	j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=	'//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);	})(window,document,'script','dataLayer','GTM-PGNCT7'); 0'''
r = cn.arrange(sent)
print(len(r['index']))
print(len(r['word']))
print(r['normalizedNER'])