import syft as sy
import torch as th
hook = sy.TorchHook(th)
pub,pri = sy.keygen()
x= th.tensor([1,2,3]).encrypt('pailler' , public_key=pub)
y = th.tensor([2,2,2]).encrypt('paillier', public_key=pub)
sum = x + y
sum.dcrypt('paillier', private_key=pri)
