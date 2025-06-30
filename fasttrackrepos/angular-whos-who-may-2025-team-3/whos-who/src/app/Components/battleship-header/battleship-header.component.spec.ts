import { ComponentFixture, TestBed } from '@angular/core/testing';

import { BattleshipHeaderComponent } from './battleship-header.component';

describe('BattleshipHeaderComponent', () => {
  let component: BattleshipHeaderComponent;
  let fixture: ComponentFixture<BattleshipHeaderComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [BattleshipHeaderComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(BattleshipHeaderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
