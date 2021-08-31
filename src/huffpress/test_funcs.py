import filecmp
from shutil import copyfile

from huffpress.compress import compress
from huffpress.decompress import decompress
from huffpress.decorators import comp, decomp
from huffpress.generic import Mode


def string_test(inp_txt):
    comp_var = compress(inp_txt)
    decomp_var = decompress(comp_var)
    dec_txt = "".join(map(chr, list(decomp_var)))
    return inp_txt == dec_txt


@comp
def decorator_comp_test():
    return LONG_TEXT


@decomp("in_var")
def decorator_decomp_test(in_var):
    return in_var


def compress_test(filename, mode=Mode.DEFAULT):
    copyfile(filename, f"{filename}.bak")
    compress(filename, mode=mode, verbose=True)
    decompress(f"{filename}.hac", verbose=True)
    return filecmp.cmp(f"{filename}.bak", filename)


LONG_TEXT = "This will be compressed  and then decompressed by the huffman algorithm. "\
            "What is holding up the public confirmation of whether it is Russell or Bottas is unclear, "\
            "but the suspicion is that Wolff wants the Finn's future firmed up first. "\
            "The Blues, who lost N'Golo Kante to injury, brought on Thiago Silva and Mateo Kovacic and "\
            "held the hosts at bay with a superbly drilled defensive display, goalkeeper Edouard Mendy playing "\
            "his part by saving well from Virgil van Dijk and Fabinho, with Diogo Jota also coming close "\
            "with a headed chance.Klopp also showed his huge faith in 18-year-old Harvey Elliott, starting the "\
            "youngster in a match of such consequence against the European champions. He showed some nice touches "\
            "that promise so much for the future. In the event that the Purchaser defaults in the payment of "\
            "any instalment of purchase price, taxes, insurance, interest, or the annual charge described "\
            "elsewhere herein, or shall default in the performance of any other obligations set forth in this "\
            "Contract, the Seller may: at his option: (a) Declare immediately due and payable the entire unpaid "\
            "balance of purchase price, with accrued interest, taxes, and annual charge, and demand full payment "\
            "thereof, and enforce conveyance of the land by termination of the contract or according to the terms "\
            "hereof, in which case the Purchaser shall also be liable to the Seller for reasonable attorney's "\
            "fees for services rendered by any attorney on behalf of the Seller, or (b) sell said land and premises "\
            "or any part thereof at public auction, in such manner, at such time and place, upon such terms and "\
            "conditions, and upon such public notice as the Seller may deem best for the interest of all concerned, "\
            "consisting of advertisement in a newspaper of general circulation in the county or city in which the "\
            "security property is located at least once a week for Three (3) successive weeks or for such period "\
            "as applicable law may require and, in case of default of any purchaser, to re-sell with such "\
            "postponement of sale or resale and upon such public notice thereof as the Seller may determine, "\
            "and upon compliance by the Purchaser with the terms of sale, and upon judicial approval as may be "\
            "required by law, convey said land and premises in fee simple to and at the cost of the Purchaser, who shall not be liable to see to the application of the purchase money; and from the proceeds of the sale: First to pay all proper costs and charges, including but not limited to court costs, advertising expenses, auctioneer's allowance, the expenses, if any required to correct any irregularity in the title, premium for Seller's bond, auditor's fee, attorney's fee, and all other expenses of sale occurred in and about the protection and execution of this contract, and all moneys advanced for taxes, assessments, insurance, and with interest thereon as provided herein, and all taxes due upon said land and premises at time of sale, and to retain as compensation a commission of five percent (5%) on the amount of said sale or sales; SECOND, to pay the whole amount then remaining unpaid of the principal of said contract, and interest thereon to date of payment, whether the same shall be due or not, it being understood and agreed that upon such sale before maturity of the contract the balance thereof shall be immediately due and payable; THIRD, to pay liens of record against the security property according to their priority of lien and to the extent that funds remaining in the hands of the Seller are available; and LAST, to pay the remainder of said proceeds, if any, to the vendor, his heirs, personals representatives, successors or assigns upon the delivery and surrender to the vendee of possession of the land and premises, less costs and excess of obtaining possession."
