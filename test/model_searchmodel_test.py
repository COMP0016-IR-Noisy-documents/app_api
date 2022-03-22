
import test.result.constance as const
import pytest
from source.model.searchModel import searchModel
'''
search model unit test
'''
sm = searchModel()
class TestMetadata:
    def test_add_metadata_to_doc(self):
        
        meta = sm.get_metadata(1)
        print("meta")
        assert meta["url"] == "http://hydro.ijs.si/v014/6e/nzbynfzw3umn4kkfclqyu6jeuhhxu2vf.pdf"
        #assert meta['description'] == "“Cinema is the art of moving image destruction,” says Paolo Cherchi Usai. Although he claims that a\r\nfilm is condemned to degradation due to the damage acquired during each projection, this judgement\r\ncould also refer to the low sustainability of film, caused by its material form.\r\n\r\nThis appeared in various historical ruptures, which have proved short life-span to be an immanent\r\ncharacteristic of the filmic base because of its chemical structure. After a big number of archives\r\nburned in devastating fires due to the high inflammability of the nitrate base, the latter was replaced by\r\nthe triacetate celluloid carrier as a more sustainable medium. However, shortly after the discovery, the\r\ntriacetate base started showing signs of rapid degradation accompanied by emissions of acid fumes\r\ninto the air that surrounds the degraded material. The resulting distinctive smell contributed to terming\r\nthis process of decay vinegar syndrome or the illness of triacetate film. The process is irreversible and\r\ninevitable – at best, it can only be decelerated by maintaining the proper storage conditions in climate\r\ncontrolled vaults. The main action that can be taken is the timely evaluation of the state of the\r\ncollection, which can be performed with pH indicator strips and followed by the optimization of storage\r\nconditions. Nowadays, when celluloid film on triacetate base represents the large-scale portion of\r\nmoving image collections, the vinegar syndrome is a critical issue that is affecting a great deal of\r\naudiovisual heritage institutions. One of the solutions for the preservation of elements in precarious\r\nstate lies in scanning and migration to the digital medium. However, this action should not be taken\r\nwithout being preceded by the appropriate conservation strategies. The long-term preservation of\r\ndegraded materials can only be assured by the assessment of the degradation state and prioritization\r\nof elements based on their condition."
