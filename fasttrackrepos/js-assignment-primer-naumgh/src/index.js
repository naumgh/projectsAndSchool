export function calculateTotal (items, tax) {
  console.log(items, tax);
  // TODO
  let total = 0;
  let valid_tax = 0;
  if (typeof tax === 'number') {
    valid_tax = Math.abs(tax);
  }
  for (let item of items) {
    if(item.taxable === true && valid_tax > 0){
      total += item.price + item.price * valid_tax;
    }else{
      total += item.price;
    }
  }
  return total;
}
