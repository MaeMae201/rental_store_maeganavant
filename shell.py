#the built in functions input() and print() can only be called in the SHELL!!<<<>>>>
import core
import disk
import time,sys
from subprocess import check_output
speak = check_output(['espeak','Welcome to Maegans New Orleans themed Party Rentals!'])
typing_speed = 12
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(typing_speed / 970.0)
    return input()
def main():
    print(slow_type(' 🎭𝓦𝓮𝓵𝓬𝓸𝓶𝓮 𝓽𝓸 𝓜𝓪𝓮𝓰𝓪𝓷𝓼 𝓝𝓮𝔀 𝓞𝓻𝓵𝓮𝓪𝓷𝓼 𝓣𝓱𝓮𝓶𝓮𝓭 𝓟𝓪𝓻𝓽𝔂 𝓡𝓮𝓷𝓽𝓪𝓵𝓼🎭 '))
    print(slow_type('𝓘 𝓱𝓸𝓹𝓮 𝔂𝓸𝓾 𝓯𝓲𝓷𝓭 𝔀𝓱𝓪𝓽 𝔂𝓸𝓾𝓻𝓮 𝓵𝓸𝓸𝓴𝓲𝓷𝓰 𝓯𝓸𝓻 ❗ 𝓗𝓪𝓿𝓮 𝓪 𝓖𝓻𝓮𝓪𝓽 𝓭𝓪𝔂! 🎉'))
    deposit = slow_type('𝓔𝓪𝓬𝓱  𝓬𝓾𝓼𝓽𝓸𝓶𝓮𝓻 𝔀𝓲𝓵𝓵  𝓱𝓪𝓿𝓮  𝓽𝓸  𝓹𝓪𝔂 𝓪 𝓭𝓮𝓹𝓸𝓼𝓲𝓽 𝓸𝓯  $25 𝓯𝓸𝓻 𝓮𝓪𝓬𝓱 𝓼𝓪𝓵𝓮')
    purchase = slow_type('𝓘𝓼 𝓽𝓱𝓲𝓼 𝓶𝓮𝓽𝓱𝓸𝓭 𝓸𝓴𝓪𝔂 𝔀𝓲𝓽𝓱 𝔂𝓸𝓾?(𝓨\𝓝)')
    if purchase == 'y':
        print(slow_type('\n𝓨𝓸𝓾𝓻 𝓶𝓸𝓷𝓮𝔂 𝔀𝓲𝓵𝓵 𝓫𝓮 𝓻𝓮𝓽𝓾𝓻𝓷𝓮𝓭 𝓸𝓷𝓬𝓮 𝓽𝓱𝓮 𝓹𝓻𝓸𝓭𝓾𝓬𝓽 𝓲𝓼 𝓲𝓷𝓼𝓹𝓮𝓬𝓽𝓮𝓭 𝓪𝓷𝓭 𝓷𝓸𝓽 𝓭𝓪𝓶𝓪𝓰𝓮𝓭\n'))
    elif purchase == 'n':
        print(slow_type('𝓢𝓸𝓻𝓻𝔂 𝓨𝓸𝓾 𝓬𝓪𝓷𝓽 𝓻𝓮𝓷𝓽 𝓪𝓷𝔂𝓽𝓱𝓲𝓷𝓰 𝓾𝓷𝓵𝓮𝓼𝓼 𝔂𝓸𝓾 𝓹𝓪𝔂 𝓽𝓱𝓮 𝓭𝓮𝓹𝓸𝓼𝓲𝓽.'))
        return None
    party_inventory = ['::::\t1.𝓜𝓪𝓻𝓭𝓲 𝓖𝓻𝓪𝓼 𝓜𝓪𝓼𝓴𝓼 $3.50','::::\t2.𝓞𝓾𝓽𝓭𝓸𝓸𝓻 𝓦𝓸𝓸𝓭𝓮𝓷 𝓓𝓪𝓷𝓬𝓮 𝓕𝓵𝓸𝓸𝓻 $50.00', '::::\t3.𝓒𝓪𝓷 𝓵𝓲𝓰𝓱𝓽𝓼 $2.50','::::\t4.𝓜𝓪𝓻𝓭𝓲 𝓖𝓻𝓪𝓼 𝓢𝓽𝓻𝓮𝓮𝓽𝓼 𝓢𝓲𝓰𝓷𝓼 $5.00', '::::\t5.𝓑𝓾𝓲𝓵𝓭𝓲𝓷𝓰 𝓟𝓻𝓸𝓹𝓼 $25.00']
    print(*party_inventory,sep='\n')
    purchase = slow_type('\n 𝓣𝓸 𝓶𝓪𝓴𝓮 𝓪 𝓼𝓮𝓵𝓮𝓬𝓽𝓲𝓸𝓷 𝓽𝔂𝓹𝓮 𝓲𝓷 𝓽𝓱𝓮 𝓷𝓾𝓶𝓫𝓮𝓻 𝓵𝓲𝓼𝓽𝓮𝓭 𝓫𝔂 𝓽𝓱𝓮 𝓲𝓽𝓮𝓶. \n')
    days = slow_type('\n 𝓗𝓸𝔀 𝓶𝓪𝓷𝔂 𝓭𝓪𝔂𝓼 𝔀𝓲𝓵𝓵 𝔂𝓸𝓾 𝓫𝓮 𝓻𝓮𝓷𝓽𝓲𝓷𝓰 𝓽𝓱𝓲𝓼 𝓹𝓻𝓸𝓭𝓾𝓬𝓽? \n')
    print(slow_type('\n 𝓣𝓸𝓽𝓪𝓵 𝓒𝓸𝓼𝓽:${:.2f}'))
    print(slow_type('\n 𝓣𝓱𝓪𝓷𝓴𝓼! 𝓟𝓪𝓻𝓽𝔂 𝓞𝓷....𝔀/𝓸𝓾𝓽 𝓽𝓱𝓮 𝓿𝓸𝓸𝓭𝓸𝓸 \n'))

    f = open('history.txt','r')
    if f.mode == 'r':
        contents = f.read()
        print (contents)
    f = open('inventory.txt','r')
    if f.mode == 'r':
        contents = f.read()
        print (contents)

    if purchase == 'restock':
        print(core.restock())
        return None
    if purchase == 'revenue':
        print('𝓨𝓸𝓾𝓻 𝓽𝓸𝓽𝓪𝓵 𝓻𝓮𝓿𝓮𝓷𝓾𝓮 𝓲𝓼 ${:.2f}'.format(core.revenue()))
        return None
   
    # disk.make_history()
    # disk.make_history_2
    # disk.inventory()
    # core.compute_bill()
    # core.shopping_inven()
    core.sales_tax_other()

if __name__ == '__main__':
    main()