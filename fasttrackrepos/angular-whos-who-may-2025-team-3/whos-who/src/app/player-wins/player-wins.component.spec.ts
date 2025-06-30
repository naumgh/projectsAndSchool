import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PlayerWinsComponent } from './player-wins.component';

describe('PlayerWinsComponent', () => {
  let component: PlayerWinsComponent;
  let fixture: ComponentFixture<PlayerWinsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PlayerWinsComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PlayerWinsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
